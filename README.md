# 🔐 Phishing URL Detection System

A **full-stack machine learning web application** that detects phishing URLs in real time using handcrafted URL features, a trained ML model, and a modern React frontend.

---

## 🚀 Overview

Phishing attacks are among the most common and dangerous cybersecurity threats today.  
This project provides a **real-time phishing URL detection system** that analyzes URLs and classifies them as:

- ✅ **Legitimate**
- 🚨 **Phishing**

The system combines **Machine Learning**, **FastAPI**, and **React** to deliver an end-to-end cybersecurity solution with explainability and scan history support.

---

## 🧠 How It Works

1. The user enters a URL in the web interface  
2. URL features are extracted, such as:
   - URL length
   - Number of digits
   - Special characters
   - Subdomains
   - Suspicious keywords
3. A trained **Random Forest classifier** predicts the phishing probability  
4. A **risk level** (Low / Medium / High) is assigned based on thresholds  
5. Results are displayed instantly with explanations  
6. Scan history is stored in a database and can be viewed or cleared  
7. Trusted domains (Google, GitHub, OpenAI, etc.) are whitelisted and bypass the ML model  

---

## 🛠️ Tech Stack

### 🔹 Frontend
- React (JavaScript)
- HTML, CSS
- Fetch API
- Dark / Light Mode UI

### 🔹 Backend
- FastAPI
- Python
- SQLite (scan history storage)
- Joblib (model persistence)

### 🔹 Machine Learning
- Scikit-learn
- Random Forest Classifier
- Hand-engineered URL features
- Probability-based risk scoring

---

## ✨ Features

- Real-time phishing URL detection  
- Risk levels: **Low / Medium / High**  
- ML Risk Score (confidence percentage)  
- Feature-based explanations  
- Scan history with database storage  
- Clear scan history option  
- Dark / Light mode UI  
- Trusted domain whitelist  
- Invalid URL handling  

---

## 📂 Project Structure

```text
Phishing_Detection/
├── backend/
│   └── ml_api/
│       ├── app.py
│       ├── database.py
│       ├── explanation.py
│       ├── feature_extractor.py
│       ├── phishing_rf_final.pkl
│       ├── feature_columns.pkl
│       └── scans.db
├── frontend/
│   └── phishing_ui/
│       ├── public/
│       └── src/
│           ├── App.jsx
│           ├── App.css
│           └── index.js
└── README.md
```
## ▶️ How to Run Locally

Follow the steps below to run the project on your local machine.

---

### 1️⃣ Backend (FastAPI)

Open a terminal and navigate to the backend directory:

```bash
cd backend/ml_api
Install the required Python dependencies:

bash
pip install -r requirements.txt
Start the FastAPI server:

bash
python -m uvicorn app:app --reload
The backend API will be available at:

cpp
http://127.0.0.1:8000
You can also access the interactive API documentation at:

arduino
http://127.0.0.1:8000/docs
```
2️⃣ Frontend (React)
Open a new terminal window and navigate to the frontend directory:

```bash
cd frontend/phishing_ui
Install frontend dependencies:

bash
npm install
Start the React development server:

bash
npm start
The frontend application will run at:

arduino
http://localhost:3000
```
🧪 Example Test URLs
Use the following URLs to test the application:

https://secure-login-paypal-update.com → 🚨 Phishing

https://www.google.com → ✅ Legitimate

http://free-gift-card123.net → 🚨 Phishing

📊 Model Performance
Accuracy: ~80–85%

ROC-AUC: ~0.90

Training Dataset: 800,000+ URLs

Balanced precision and recall

