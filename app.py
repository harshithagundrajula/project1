from flask import Flask, request, jsonify
from model import predict_risk
from rag_agent import generate_explanation

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Credit Risk System Running 🚀"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    income = data['income']
    loan = data['loan']
    credit_score = data['credit_score']

    risk, probability = predict_risk(income, loan, credit_score)
    explanation = generate_explanation(income, loan, credit_score)

    return jsonify({
        "risk": int(risk),
        "risk_probability": round(probability, 2),
        "explanation": explanation
    })

if __name__ == '__main__':
    app.run(debug=True)
