from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from urllib.parse import urlparse

from feature_extractor import extract_features
from explanation import explain_features
from database import init_db, get_connection

# LOAD MODEL 
model = joblib.load("phishing_rf_final.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# TRUSTED DOMAINS 
TRUSTED_DOMAINS = [
    "google.com",
    "youtube.com",
    "github.com",
    "microsoft.com",
    "amazon.com",
    "chatgpt.com",
    "openai.com"
]

# -------------------- APP INIT --------------------
app = FastAPI(title="Phishing URL Detection API")

# -------------------- CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- DB INIT --------------------
init_db()

# -------------------- SCHEMA 
class URLRequest(BaseModel):
    url: str

# ROUTES 
@app.get("/")
def root():
    return {"status": "ML API running"}

@app.post("/predict")
def predict_url(data: URLRequest):

    # INPUT VALIDATION 
    if not data.url.startswith(("http://", "https://")):
        return {
            "url": data.url,
            "prediction": "Invalid URL",
            "risk_level": "Unknown",
            "ml_risk_score": None,
            "explanations": ["Input is not a valid URL"]
        }

    # DOMAIN EXTRACTION 
    domain = urlparse(data.url).netloc.lower().split(":")[0]

    # WHITELIST 
    if any(domain.endswith(td) for td in TRUSTED_DOMAINS):

    # SAVE WHITELISTED SCAN
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO scans (url, prediction, risk_level, ml_risk_score) VALUES (?, ?, ?, ?)",
            (data.url, "Legitimate", "Low", 0.01)
        )
        conn.commit()
        conn.close()

        return {
            "url": data.url,
            "prediction": "Legitimate",
            "risk_level": "Low",
            "ml_risk_score": 0.01,
            "reason": "Trusted domain whitelist"
        }


    # FEATURE EXTRACTION 
    features = extract_features(data.url)
    X = pd.DataFrame([features])
    X = X.reindex(columns=feature_columns, fill_value=0)

    # ML PREDICTION
    prob = model.predict_proba(X)[0][1]

    # RISK LOGIC 
    if prob < 0.4:
        risk = "Low"
        prediction = "Legitimate"
    elif prob < 0.7:
        risk = "Medium"
        prediction = "Suspicious"
    else:
        risk = "High"
        prediction = "Phishing"

    # EXPLANATIONS 
    reasons = explain_features(features)

    # SAVE TO DB 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO scans (url, prediction, risk_level, ml_risk_score) VALUES (?, ?, ?, ?)",
        (data.url, prediction, risk, float(prob))
    )
    conn.commit()
    conn.close()

    return {
        "url": data.url,
        "prediction": prediction,
        "risk_level": risk,
        "ml_risk_score": round(float(prob), 4),
        "explanations": reasons
    }

@app.get("/history")
def get_history():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT url, prediction, risk_level, ml_risk_score, timestamp
        FROM scans
        ORDER BY timestamp DESC
        LIMIT 20
        """
    )
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "url": r[0],
            "prediction": r[1],
            "risk_level": r[2],
            "ml_risk_score": r[3],
            "timestamp": r[4]
        }
        for r in rows
    ]
@app.delete("/history")
def clear_history():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM scans")
    conn.commit()
    conn.close()
    return {"status": "History cleared"}
