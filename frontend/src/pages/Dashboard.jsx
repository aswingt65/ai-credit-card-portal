import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const cardBackgrounds = [
  "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
  "linear-gradient(135deg, #f6d365 0%, #fda085 100%)",
  "linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%)",
  "linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%)",
];

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

// Temporary in-memory storage for additional limits
const limitStorage = {};

export default function Dashboard() {
  const navigate = useNavigate();
  const [cards, setCards] = useState([]);
  const [transactions, setTransactions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [selectedCard, setSelectedCard] = useState(null);
  const [manageCard, setManageCard] = useState(null);
  const [newLimits, setNewLimits] = useState({
    total: "",
    epos: "",
    shopping: "",
    international: "",
  });
  const [currentPage, setCurrentPage] = useState(1);
  const txnsPerPage = 5;
  const [sortConfig, setSortConfig] = useState({ key: "date", direction: "asc" });

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await axios.get("http://127.0.0.1:5000/api/credit-cards");
        setCards(res.data);
        setLoading(false);
      } catch {
        setError("Failed to fetch cards");
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  useEffect(() => {
    async function fetchTransactions() {
      if (!selectedCard) return;
      setLoading(true);
      try {
        const res = await axios.get("http://127.0.0.1:5000/api/transactions");
        const filtered = res.data.filter((t) => t.card_id === selectedCard.id);
        setTransactions(filtered);
        setCurrentPage(1);
        setLoading(false);
      } catch {
        setError("Failed to fetch transactions");
        setLoading(false);
      }
    }
    fetchTransactions();
  }, [selectedCard]);

  useEffect(() => {
    // Set defaults for manage card limits if stored
    if (manageCard) {
      const saved = limitStorage[manageCard.id] || {
        epos: "",
        shopping: "",
        international: "",
      };
      setNewLimits({
        total: manageCard.credit_limit,
        ...saved,
      });
    }
  }, [manageCard]);

  const categoryData = Object.values(
    transactions.reduce((acc, txn) => {
      acc[txn.category] = acc[txn.category] || { name: txn.category, value: 0 };
      acc[txn.category].value += txn.amount;
      return acc;
    }, {})
  );

  const sortTransactions = (txns) => {
    if (!sortConfig.key) return txns;
    return [...txns].sort((a, b) => {
      const aValue = a[sortConfig.key];
      const bValue = b[sortConfig.key];
      if (aValue < bValue) return sortConfig.direction === "asc" ? -1 : 1;
      if (aValue > bValue) return sortConfig.direction === "asc" ? 1 : -1;
      return 0;
    });
  };

  const handleSort = (key) => {
    setSortConfig((prev) => ({
      key,
      direction: prev.key === key && prev.direction === "asc" ? "desc" : "asc",
    }));
  };

  const sortedTxns = sortTransactions(transactions);
  const totalPages = Math.ceil(sortedTxns.length / txnsPerPage);
  const paginatedTxns = sortedTxns.slice(
    (currentPage - 1) * txnsPerPage,
    currentPage * txnsPerPage
  );

  const handleToggleStatus = async (card) => {
    const updatedStatus = card.status === "active" ? false : true;

try {
  await axios.put(`http://127.0.0.1:5000/api/credit-cards/${card.id}/status`, {
    active: updatedStatus,
  });

  const updatedCard = {
    ...card,
    status: updatedStatus ? "active" : "inactive", // Update locally to match
  };

  setManageCard(updatedCard);
  setCards((prev) =>
    prev.map((c) => (c.id === card.id ? updatedCard : c))
  );
} catch (err) {
  console.error("Failed to update status:", err);
  alert("Failed to update card status.");
}
  };

  const handleLimitUpdate = async () => {
    try {
      const payload = {
        total: parseFloat(newLimits.total) || 0,
      };
      await axios.put(
        `http://127.0.0.1:5000/api/credit-cards/${manageCard.id}/limits`,
        payload
      );

      // Update local card data
      setCards((prev) =>
        prev.map((c) =>
          c.id === manageCard.id ? { ...c, credit_limit: payload.total } : c
        )
      );
      setManageCard((prev) => ({
        ...prev,
        credit_limit: payload.total,
      }));

      // Save extra limits to local storage
      limitStorage[manageCard.id] = {
        epos: newLimits.epos,
        shopping: newLimits.shopping,
        international: newLimits.international,
      };

      alert("Limits updated successfully!");
    } catch (err) {
      console.error("Failed to update limits:", err);
      alert("Failed to update card limits.");
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

      {/* Manage Card Section */}
      {manageCard ? (
        <div className="max-w-3xl mx-auto p-6 bg-white rounded-xl shadow-lg mt-8">
          <h2 className="text-2xl font-bold mb-4 text-center">Manage Card: {manageCard.card_number}</h2>
          <div className="mb-4">
            <label className="block text-lg font-semibold mb-2">Card Status</label>
            <label className="inline-flex items-center cursor-pointer">
              <span className="mr-3 font-medium text-gray-700">Inactive</span>
              <div className="relative">
                <input
                  type="checkbox"
                  className="sr-only peer"
                  checked={manageCard.status === "active"}
                  onChange={() => handleToggleStatus(manageCard)}
                />
                <div className="w-11 h-6 bg-gray-300 rounded-full peer peer-checked:bg-green-500 transition-all duration-300"></div>
                <div className="absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full transition-transform duration-300 peer-checked:translate-x-full"></div>
              </div>
              <span className="ml-3 font-medium text-gray-700">Active</span>
            </label>
          </div>

          <div className="space-y-4 mb-6">
            {["total", "epos", "shopping", "international"].map((type) => (
              <div key={type}>
                <label className="block text-sm font-semibold capitalize">
                  {type} Limit
                </label>
                <input
                  type="number"
                  value={newLimits[type]}
                  onChange={(e) => setNewLimits((prev) => ({ ...prev, [type]: e.target.value }))}
                  placeholder={`Enter ${type} limit`}
                  className="w-full p-2 border rounded-md focus:ring-2 ring-blue-400"
                />
              </div>
            ))}
          </div>

          <div className="flex justify-between">
            <button
              className="px-6 py-2 rounded-full bg-gradient-to-r from-indigo-500 to-purple-600 text-white shadow-md hover:scale-105 transition"
              onClick={handleLimitUpdate}
            >
              Update Limits
            </button>
            <button
              className="px-6 py-2 rounded-full border border-gray-500 text-gray-700 hover:bg-gray-100"
              onClick={() => setManageCard(null)}
            >
              Go Back to Dashboard
            </button>
          </div>
        </div>
      ) : !selectedCard ? (
        <>
          <h3 className="text-4xl font-bold text-center text-gray-800 mb-10">
            Your Credit Cards
          </h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8 h-64">
  {cards.map((card, idx) => (
    <div
      key={card.id}
      className="relative bg-white/10 backdrop-blur-md rounded-2xl overflow-hidden border border-white/20 shadow-2xl transition-transform transform hover:scale-105"
      style={{ background: cardBackgrounds[idx % cardBackgrounds.length] }}
    >
      <div className="p-6 flex flex-col justify-between h-60 text-white">
        <div>
          <p className="text-xl font-mono tracking-widest mb-2">{card.card_number}</p>
          <p className="uppercase font-semibold text-lg">{card.card_type}</p>
          <p className="text-sm opacity-90 mt-1">Expires {card.expiry}</p>
        </div>

        <div className="mt-4">
          <p className="text-sm">
            Credit Limit: <span className="font-bold">${card.credit_limit.toLocaleString()}</span>
          </p>
          <p className="text-sm">
            Available: <span className="font-bold">${card.available_credit.toLocaleString()}</span>
          </p>

          <div className="flex justify-between items-center gap-3 mt-4">
            <button
              onClick={() => setSelectedCard(card)}
              className="bg-gradient-to-r from-indigo-500 to-purple-600 text-white font-semibold rounded-full px-2 py-2 hover:brightness-110 shadow-md transition"
            >
              View Transactions
            </button>
            <button
              onClick={() => setManageCard(card)}
              className="bg-gradient-to-r from-pink-500 to-red-500 text-white font-semibold rounded-full px-2 py-2 hover:brightness-110 shadow-md transition"
            >
              Manage Card
            </button>
          </div>
        </div>
      </div>
    </div>
  ))}
</div>

        </>
      ) : (
        <>
          <div className="flex justify-between items-center mb-6 max-w-6xl mx-auto">
            <button
              onClick={() => setSelectedCard(null)}
              className="px-5 py-2 rounded-lg bg-indigo-600 text-white font-semibold hover:bg-indigo-700"
            >
              ← Back to Cards
            </button>
          </div>

          <div className="bg-white rounded-xl shadow-md p-6 mb-10 max-w-6xl mx-auto">
            <h2 className="text-2xl font-bold text-gray-900 mb-2">
              {selectedCard.card_type} Card Ending in{" "}
              {selectedCard.card_number.slice(-4)}
            </h2>
            <div className="text-gray-700 text-sm space-y-1">
              <p>
                Expiry: <strong>{selectedCard.expiry}</strong>
              </p>
              <p>
                Credit Limit:{" "}
                <strong>${selectedCard.credit_limit.toLocaleString()}</strong>
              </p>
              <p>
                Available Credit:{" "}
                <strong className="text-green-600">
                  ${selectedCard.available_credit.toLocaleString()}
                </strong>
              </p>
            </div>
          </div>

          {categoryData.length > 0 && (
            <div className="mb-12 max-w-5xl mx-auto">
              <h3 className="text-xl font-bold text-gray-800 mb-4 text-center">
                Spending by Category
              </h3>
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                  <Pie
                    data={categoryData}
                    dataKey="value"
                    nameKey="name"
                    cx="50%"
                    cy="50%"
                    outerRadius={100}
                    label
                  >
                    {categoryData.map((entry, index) => (
                      <Cell key={index} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                  <Legend />
                </PieChart>
              </ResponsiveContainer>
            </div>
          )}

          <div className="overflow-x-auto bg-white shadow-lg rounded-xl max-w-6xl mx-auto mb-10">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-indigo-600 text-white text-sm uppercase">
                <tr>
                  {["date", "description", "amount", "category"].map((key) => (
                    <th
                      key={key}
                      className={`py-3 px-6 text-left cursor-pointer`}
                      onClick={() => handleSort(key)}
                    >
                      {key.charAt(0).toUpperCase() + key.slice(1)}{" "}
                      {sortConfig.key === key ? (sortConfig.direction === "asc" ? "↑" : "↓") : ""}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody className="text-gray-700 text-sm">
                {paginatedTxns.map((txn, idx) => (
                  <tr
                    key={txn.id}
                    className={`border-t ${idx % 2 === 0 ? "bg-gray-50" : "bg-white"}`}
                  >
                    <td className="py-3 px-6 font-mono">{txn.date}</td>
                    <td className="py-3 px-6">{txn.description}</td>
                    <td className="py-3 px-6 text-right text-green-700 font-semibold">
                      ${txn.amount.toFixed(2)}
                    </td>
                    <td className="py-3 px-6">{txn.category}</td>
                  </tr>
                ))}
              </tbody>
            </table>

            {/* Pagination */}
            <div className="flex justify-center gap-2 py-6">
  {Array.from({ length: totalPages }, (_, i) => i + 1).map((pg) => (
    <button
      key={pg}
      onClick={() => setCurrentPage(pg)}
      className={`px-4 py-2 rounded-full font-medium transition duration-200 shadow-sm border ${
        pg === currentPage
          ? "bg-gradient-to-r from-indigo-500 to-purple-600 text-white border-transparent shadow-lg scale-105"
          : "bg-white text-indigo-700 border-indigo-300 hover:bg-indigo-50 hover:border-indigo-500"
      }`}
    >
      {pg}
    </button>
  ))}
</div>
          </div>
        </>
      )}
    </div>
  );
}
