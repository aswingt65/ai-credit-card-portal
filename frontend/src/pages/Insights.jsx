import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  PieChart, Pie, Cell, Tooltip, BarChart, Bar, XAxis, YAxis,
  CartesianGrid, Legend, ResponsiveContainer
} from 'recharts';
import { useNavigate } from 'react-router-dom';

const COLORS = [
  "#8884d8",
  "#82ca9d",
  "#ffc658",
  "#ff7f50",
  "#a4de6c",
  "#d0ed57",
  "#8dd1e1",
  "#83a6ed",
];
const Insights = () => {
  const navigate = useNavigate();
  const [insights, setInsights] = useState('');
  const [offers, setOffers] = useState('');
  const [categoryData, setCategoryData] = useState([]);

  useEffect(() => {
    fetchInsights();
    fetchOffers();
    fetchTransactions();
  }, []);

  const fetchInsights = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/ai/insights');
      setInsights(response.data.insights);
    } catch (err) {
      setInsights('Error fetching insights.');
    }
  };

  const fetchOffers = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/ai/offers');
      setOffers(response.data.offers);
    } catch (err) {
      setOffers('Error fetching offers.');
    }
  };

  const fetchTransactions = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/transactions');
      const categoryTotals = {};

      response.data.forEach((txn) => {
        categoryTotals[txn.category] = (categoryTotals[txn.category] || 0) + txn.amount;
      });

      const chartData = Object.entries(categoryTotals).map(([category, amount]) => ({
        category,
        amount,
      }));

      setCategoryData(chartData);
    } catch (err) {
      console.error('Failed to load transactions', err);
    }
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
            <button onClick={() => navigate("/chatbot")} className="nav-btn purple">Ask Chatbot</button>
          </div>
        </div>
      </nav>
      
      <h2 className="text-3xl font-bold mb-6">📊 AI-Powered Financial Insights</h2>

      {/* Charts Row */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-9 mb-9">
        <div className="bg-white p-4 rounded shadow">
          <h3 className="text-xl font-semibold mb-4">Bar Chart: Category-wise Spending</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={categoryData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="category" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="amount" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white p-4 rounded shadow">
          <h3 className="text-xl font-semibold mb-4">Pie Chart: Spending Distribution</h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={categoryData}
                dataKey="amount"
                nameKey="category"
                cx="50%"
                cy="50%"
                outerRadius={100}
                fill="#8884d8"
                label
              >
                {categoryData.map((_, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Insights and Offers Row */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="bg-white p-4 rounded shadow">
          <h3 className="text-xl font-semibold mb-4">💬 Spending Insights</h3>
          <p className="whitespace-pre-wrap text-gray-700">{insights}</p>
        </div>

        <div className="bg-white p-4 rounded shadow">
          <h3 className="text-xl font-semibold mb-4">🎁 Personalized Offers</h3>
          <p className="whitespace-pre-wrap text-gray-700">{offers}</p>
        </div>
      </div>
    </div>
  );
};

export default Insights;
