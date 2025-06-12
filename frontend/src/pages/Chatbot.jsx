import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


const Chatbot = () => {
    const navigate = useNavigate();
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');

    try {
      const response = await axios.post('http://localhost:5000/api/chat', {
        message: input
      });

      const botMessage = {
        sender: 'bot',
        text: response.data.response
      };
      setMessages(prev => [...prev, botMessage]);
    } catch (err) {
      setMessages(prev => [...prev, { sender: 'bot', text: 'Error fetching response.' }]);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 w-full">
   <nav className="navbar">
  <div className="navbar-container">
    <div className="navbar-title ">💳 CreditWise</div>
    <div className="navbar-buttons">
      <button onClick={() => navigate("/")} className="nav-btn">
        Dashboard
      </button>
      <button onClick={() => navigate("/insights")} className="nav-btn">
  Insights & Offers
</button>
      <button onClick={() => navigate("/health")} className="nav-btn">Credit Health & Impacts</button>
      <button onClick={() => navigate("/chatbot")} className="nav-btn purple">
        Ask Chatbot
      </button>
    </div>
  </div>
</nav>
      <h2 className="text-2xl font-bold mb-4">💬 Financial Assistant</h2>
      <div className="border p-4 h-96 overflow-y-auto rounded-lg bg-gray-50 mb-4 shadow">
        {messages.map((msg, idx) => (
          <div key={idx} className={`mb-2 ${msg.sender === 'user' ? 'text-right' : 'text-left'}`}>
            <span className={`inline-block px-3 py-2 rounded-lg ${msg.sender === 'user' ? 'bg-blue-100' : 'bg-green-100'}`}>
              {msg.text}
            </span>
          </div>
        ))}
      </div>
      <div className="flex gap-2">
        <input
          className="flex-1 border rounded p-2"
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask me about your finances..."
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
        />
        <button
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          onClick={sendMessage}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default Chatbot;
