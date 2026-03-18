import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Sample dataset
data = pd.DataFrame({
    'income': [50000, 20000, 30000, 80000, 120000, 40000, 25000, 90000],
    'loan': [20000, 15000, 25000, 30000, 50000, 20000, 18000, 40000],
    'credit_score': [700, 500, 600, 750, 800, 650, 550, 780],
    'risk': [0, 1, 1, 0, 0, 0, 1, 0]
})

X = data[['income', 'loan', 'credit_score']]
y = data['risk']

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

def predict_risk(income, loan, credit_score):
    features = [[income, loan, credit_score]]
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    return prediction, probability
