# Knowledge Base (RAG)
rules = [
    "Low credit score increases loan default risk",
    "High loan-to-income ratio increases risk",
    "High income reduces financial risk",
    "Good credit score improves loan approval chances"
]

def generate_explanation(income, loan, credit_score):
    explanation = []

    if credit_score < 600:
        explanation.append(rules[0])
    if loan > income * 0.5:
        explanation.append(rules[1])
    if income > 70000:
        explanation.append(rules[2])
    if credit_score > 700:
        explanation.append(rules[3])

    return explanation
