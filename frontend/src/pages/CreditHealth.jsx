import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import { useNavigate } from 'react-router-dom';

const CreditHealth = () => {
  const navigate = useNavigate();

  const [scenario, setScenario] = useState('');
  const [impactResult, setImpactResult] = useState('');
  const [healthResult, setHealthResult] = useState('');
  const [loadingImpact, setLoadingImpact] = useState(false);
  const [loadingHealth, setLoadingHealth] = useState(false);

  const handlePredictImpact = async () => {
    if (!scenario.trim()) return;

    setLoadingImpact(true);
    setImpactResult('');
    try {
      const res = await axios.post('http://localhost:5000/api/credit-health/predict-impact', { scenario });
      setImpactResult(res.data.impact_analysis);
    } catch (err) {
      console.error("Impact Error:", err);
      setImpactResult('Failed to fetch impact analysis.');
    }
    setLoadingImpact(false);
  };

  const handleHealthMonitor = async () => {
    setLoadingHealth(true);
    setHealthResult('');
    try {
      const res = await axios.post('http://localhost:5000/api/credit-health/monitor');
      setHealthResult(res.data.health_report);
    } catch (err) {
      console.error("Health Error:", err);
      setHealthResult('Failed to fetch health report.');
    }
    setLoadingHealth(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 w-full">
      {/* Navbar */}
      <nav className="navbar">
        <div className="navbar-container">
          <div className="navbar-title">💳 CreditWise</div>
          <div className="navbar-buttons">
            <button onClick={() => navigate("/")} className="nav-btn">Dashboard</button>
            <button onClick={() => navigate("/insights")} className="nav-btn">Insights & Offers</button>
            <button onClick={() => navigate("/health")} className="nav-btn">Credit Health & Impacts</button>
            <button onClick={() => navigate("/chatbot")} className="nav-btn">Ask Chatbot</button>
          </div>
        </div>
      </nav>

      <h2 className="text-2xl font-bold my-4">🧠 AI Credit Health Analysis</h2>

      {/* Side-by-side layout */}
      <div className="flex flex-col lg:flex-row gap-6">
        {/* Credit Score Impact */}
        <div className="bg-white p-4 rounded shadow w-full lg:w-1/2">
          <h3 className="text-xl font-semibold mb-2">📉 Credit Score Impact Prediction</h3>
          <textarea
            rows="5"
            className="w-full border p-2 rounded mb-2"
            placeholder="Describe a credit usage scenario (e.g., missing a payment, maxing out credit limit)..."
            value={scenario}
            onChange={(e) => setScenario(e.target.value)}
          />
          <button
            onClick={handlePredictImpact}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Predict Impact
          </button>
          {loadingImpact ? (
            <p className="mt-2 text-gray-500">Analyzing...</p>
          ) : (
            impactResult && <div className="mt-4"><ReactMarkdown>{impactResult}</ReactMarkdown></div>
          )}
        </div>

        {/* Credit Health Monitoring */}
        <div className="bg-white p-4 rounded shadow w-full lg:w-1/2">
          <h3 className="text-xl font-semibold mb-2">🩺 Credit Health Monitoring</h3>
          <button
            onClick={handleHealthMonitor}
            className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
          >
            Analyze Transactions
          </button>
          {loadingHealth ? (
            <p className="mt-2 text-gray-500">Analyzing your credit health...</p>
          ) : (
            healthResult && <div className="mt-4"><ReactMarkdown>{healthResult}</ReactMarkdown></div>
          )}
        </div>
      </div>
    </div>
  );
};

export default CreditHealth;
