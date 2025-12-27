import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [darkMode, setDarkMode] = useState(false);

  // Set browser tab title
  useEffect(() => {
    document.title = "Phishing URL Detector";
  }, []);

  // Scan URL
  const scanUrl = async () => {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();
      setResult(data);
    } catch {
      setError("Unable to connect to backend");
    } finally {
      setLoading(false);
    }
  };

  // Load scan history
  const loadHistory = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/history");
      const data = await response.json();
      setHistory(data);
    } catch {
      console.log("Failed to load history");
    }
  };

  // Clear scan history
  const clearHistory = async () => {
    try {
      await fetch("http://127.0.0.1:8000/history", {
        method: "DELETE",
      });
      setHistory([]);
    } catch {
      console.log("Failed to clear history");
    }
  };

  return (
    <div className={darkMode ? "app dark" : "app"}>
      <div className="container">
        <div className="content">

          {/* Dark Mode Toggle */}
          <button className="toggle" onClick={() => setDarkMode(!darkMode)}>
            {darkMode ? "☀ Light Mode" : "🌙 Dark Mode"}
          </button>

          <h1>🔐 Phishing URL Detector</h1>

          <input
            type="text"
            placeholder="Paste a URL (e.g. https://example.com)"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />

          <button onClick={scanUrl} disabled={!url || loading}>
            {loading ? "Scanning..." : "Scan URL"}
          </button>

          <button
            onClick={loadHistory}
            style={{ marginTop: "12px", background: "#64748b" }}
          >
            View Scan History
          </button>

          <button
            onClick={clearHistory}
            style={{ marginTop: "8px", background: "#ef4444" }}
            disabled={history.length === 0}
          >
            Clear History
          </button>

          {error && <p className="error">{error}</p>}

          {/* Scan Result */}
          {result && (
            <div
              className={`result ${
                result.risk_level === "High"
                  ? "danger"
                  : result.risk_level === "Medium"
                  ? "warning"
                  : "safe"
              }`}
            >
              <h2>{result.prediction}</h2>

              <p><strong>Risk Level:</strong> {result.risk_level}</p>

              <p>
                <strong>ML Risk Score:</strong>{" "}
                {(result.ml_risk_score * 100).toFixed(2)}%
              </p>

              {result.reason && <p>✔ {result.reason}</p>}

              {result.explanations && result.explanations.length > 0 && (
                <>
                  <hr />
                  <p><strong>Why this result:</strong></p>
                  <ul>
                    {result.explanations.map((e, i) => (
                      <li key={i}>⚠ {e}</li>
                    ))}
                  </ul>
                </>
              )}
            </div>
          )}

          {/* Scan History */}
          {history.length > 0 && (
            <div className="history">
              <h3>Recent Scans</h3>

              {history.map((item, index) => (
                <div key={index} className="history-item">
                  <p className="history-url">{item.url}</p>
                  <p>
                    {item.prediction} · {item.risk_level} ·{" "}
                    {(item.ml_risk_score * 100).toFixed(1)}%
                  </p>
                </div>
              ))}
            </div>
          )}

        </div>
      </div>
    </div>
  );
}

export default App;


