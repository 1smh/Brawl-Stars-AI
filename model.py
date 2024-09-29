# Decision Tree Regression Model
import pandas as pd
import joblib

def model(expLevel, power_score):
    model = joblib.load('../model.pkl')

    new_data = pd.DataFrame([[expLevel, power_score]], columns=['expLevel', 'Power 11 Score'])
    prediction = model.predict(new_data)

    return prediction[0]