🔐 Phishing URL Detection System

A full-stack machine learning web application that detects phishing URLs in real time using handcrafted URL features, a trained ML model, and a modern React frontend.

🚀 Overview

Phishing attacks are one of the most common cybersecurity threats. This project provides a real-time phishing URL detection system that analyzes URLs and classifies them as:

✅ Legitimate

🚨 Phishing

The system combines machine learning, FastAPI, and React to deliver an end-to-end cybersecurity solution.

🧠 How It Works

User enters a URL in the web interface

URL features are extracted (length, digits, special characters, subdomains, etc.)

A trained Random Forest model predicts phishing probability

Risk level is assigned based on a threshold

Results are displayed instantly with explanations

Scan history is stored and can be viewed or cleared

Trusted domains (e.g. Google, GitHub, OpenAI) are whitelisted and bypass the ML model.

🛠️ Tech Stack
🔹 Frontend

React (JavaScript)

HTML, CSS

Fetch API

Dark / Light Mode UI

🔹 Backend

FastAPI

Python

SQLite (scan history)

Joblib (model persistence)

🔹 Machine Learning

Scikit-learn

Random Forest Classifier

Hand-engineered URL features

Probability-based risk scoring

✨ Features

- Real-time phishing URL detection

- Risk levels: Low / Medium / High

- ML Risk Score (confidence)

- Feature-based explanations

- Scan history with database storage

- Clear history option

- Dark / Light mode

- Trusted domain whitelist

- Invalid URL handling

📂 Project Structure
Phishing_Detection/
│
├── backend/
│   ├── ml_api/
│   │   ├── app.py
│   │   ├── feature_extractor.py
│   │   ├── phishing_rf_final.pkl
│   │   ├── feature_columns.pkl
│   │   └── scans.db
│
├── frontend/
│   └── phishing_ui/
│       ├── src/
│       │   ├── App.jsx
│       │   ├── App.css
│       │   └── index.js
│
└── README.md

▶️ How to Run Locally
1️⃣ Backend (FastAPI)
cd backend/ml_api
python -m uvicorn app:app --reload


Backend will run at:

http://127.0.0.1:8000

2️⃣ Frontend (React)
cd frontend/phishing_ui
npm install
npm start


Frontend will run at:

http://localhost:3000

🧪 Example Test URLs
https://secure-login-paypal-update.com   → Phishing
https://www.google.com                   → Legitimate
http://free-gift-card123.net             → Phishing

📊 Model Performance

Accuracy: ~80–85%

ROC-AUC: ~0.90

Trained on 800,000+ URLs

Balanced precision and recall
