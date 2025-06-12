from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
from sample import transaction
from mock_data import credit_cards, transactions

load_dotenv()

app = Flask(__name__)
CORS(app)

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

@app.route("/api/health")
def health():
    return jsonify({"status": "Backend is up and running!"})

@app.route("/api/credit-cards")
def get_credit_cards():
    return jsonify(credit_cards)

@app.route("/api/transactions")
def get_transactions():
    return jsonify(transactions)

@app.route("/api/credit-cards/<card_id>/status", methods=["PUT"])
def update_card_status(card_id):
    data = request.get_json()
    new_status = data.get("active")

    if new_status is None:
        return jsonify({"error": "Status (active) field is required"}), 400

    for card in credit_cards:
        if card["id"] == card_id:
            card["active"] = new_status
            return jsonify({"message": "Card status updated successfully"}), 200

    return jsonify({"error": "Card not found"}), 404

@app.route("/api/credit-cards/<card_id>/limits", methods=["PUT"])
def update_credit_limits(card_id):
    data = request.get_json()
    new_limit = data.get("total")

    if not new_limit:
        return jsonify({"error": "Total limit is required"}), 400

    for card in credit_cards:
        if card["id"] == card_id:
            card["credit_limit"] = new_limit
            # Optional: update available_credit too
            return jsonify({"message": "Credit limit updated successfully"}), 200

    return jsonify({"error": "Card not found"}), 404

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')

    finance_keywords = [
        "hello", "fund", "money", "card", "credit", "debit", "loan", "interest", "bank", "investment", "stocks", "mutual fund",
        "payment", "transaction", "savings", "budget", "tax", "insurance", "mortgage", "retirement", "finance"
    ]
    if not any(keyword in user_message.lower() for keyword in finance_keywords):
        return jsonify({
            "response": "I'm trained to assist only with finance-related topics. Please ask something about banking, investments, budgeting, or credit cards."
        }), 200

    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        return jsonify({"error": "GROQ_API_KEY not found in .env"}), 500

    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [
            {
                "role": "system",
"content": (
    "You are a financial assistant. Always answer in clear, concise markdown format using:\n"
    "- Bullet points (`-` or `•`)\n"
    "- Dont use markdown\n"
    "- No long paragraphs\n"
    "- Keep it clean, professional, and readable\n"
    "- Stick strictly to financial topics. If asked non-finance questions, politely decline."
)
            },
            {"role": "user", "content": user_message}
        ],
        "model": "llama-3.1-8b-instant"
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    
    try:
        ai_message = response.json()["choices"][0]["message"]["content"]
        return jsonify({"response": ai_message})
    except Exception as e:
        return jsonify({"error": "Failed to get response from Groq API", "details": str(e)}), 500


def get_ai_response(prompt):
    data = {
        "messages": [
            {"role": "system", "content": "You are a financial assistant that analyzes transaction data."},
            {"role": "user", "content": prompt}
        ],
        "model": "llama-3.1-8b-instant"
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    try:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("Groq API Error:", response.text)  # 👈 Print full response for debugging
        raise Exception("Groq API error: " + response.text)

@app.route('/api/ai/insights', methods=['GET'])
def get_insights():
    try:
        prompt = f"Analyze the following transactions and provide categorized spending insights:\n{transaction}"
        insights = get_ai_response(prompt)
        return jsonify({"insights": insights})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/ai/offers', methods=['GET'])
def get_offers():
    try:
        category_totals = {}
        for txn in transaction:
            category = txn['category']
            category_totals[category] = category_totals.get(category, 0) + txn['amount']
        
        top_category = max(category_totals, key=category_totals.get)
        prompt = f"User has spent the most in {top_category}. Suggest personalized financial offers or rewards."
        offers = get_ai_response(prompt)
        return jsonify({"offers": offers})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/credit-health/predict-impact', methods=['POST'])
def predict_credit_score_impact():
    try:
        # Extract both score and scenario from the request
        credit_score = 720
        scenario = request.json.get("scenario", "")

        if not credit_score or not scenario:
            return jsonify({"error": "Please provide both credit_score and scenario"}), 400

        # Construct detailed prompt
        prompt = (
            f"A person with a credit score of {credit_score} is in the following situation:\n"
            f"{scenario}\n"
            f"Predict the potential impact on their credit score and explain the reasoning in detail."
        )

        headers = {
            "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
            "Content-Type": "application/json"
        }

        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are an expert AI in credit scoring. Given the credit score and behavior, predict how it will impact the user's credit score and explain why in detail."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "model": "llama-3.1-8b-instant"
        }

        # Call Groq API
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        answer = response.json()["choices"][0]["message"]["content"]

        return jsonify({"impact_analysis": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/credit-health/monitor', methods=['POST'])
def monitor_credit_health():
    try:
        prompt = f"Analyze the following credit card transaction data and provide insights on credit health: {transaction}"

        headers = {
            "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
            "Content-Type": "application/json"
        }

        payload = {
            "messages": [
                {"role": "system", "content": "You are an AI credit analyst who evaluates spending and provides credit health advice."},
                {"role": "user", "content": prompt}
            ],
            "model": "llama-3.1-8b-instant"
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        print("Groq Response:", response.text)

        insights = response.json()["choices"][0]["message"]["content"]
        return jsonify({"health_report": insights})
    
    except Exception as e:
        print("Error in /monitor:", str(e))
        return jsonify({"error": "Failed to fetch health report"}), 500

# 
if __name__ == "__main__":
    app.run(debug=True)
