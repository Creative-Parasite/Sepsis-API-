from fastapi import FastAPI, HTTPException, status, Query
import joblib
from pydantic import BaseModel
import pandas as pd
import logging


Description = """
 This API predicts the presence of Sepsis based on the provided features.
 The API supports two models: Gradient Boosting Classifier and Random Forest Classifier.
 Both models are trained on a dataset from the UCI Machine Learning Repository.

 The input data should be a JSON object with the following structure:

 {
    "prg": <float>,
    "pl": <float>,
    "pr": <float>,
    "sk": <float>,
    "ts": <float>,
    "m11": <float>,
    "bd2": <float>,
    "age": <float>,
    "insurance": "<str>"
 }

 The API returns a JSON object with the following structure:

 {
    "prediction": <bool>,
    "prediction_class": <str>
 }

 The prediction_class value is either 0 (Negative) or 1 (Positive).
 
"""
app = FastAPI(
    title= 'SEPSIS PREDICTION API',
    description= Description
)

## Load your models and encoder
gradient = joblib.load("../models/toolkit/GradientBoostingClassifier.joblib")
random_forest = joblib.load("../models/toolkit/random_forest.joblib")
encoder = joblib.load("../models/toolkit/label_encoder.joblib")

## Configure the logs
logging.basicConfig(level=logging.INFO)
logger= logging.getLogger(__name__)


## Create class features
class features(BaseModel):
    prg : float
    pl : float
    pr : float
    sk : float
    ts : float
    m11 : float
    bd2 : float
    age : float
    insurance : str
    
    
@app.get('/sepsis')
def get_sepsis():
    return {'Title': 'Sepsis prediction API'}


@app.post('/prediction', status_code=status.HTTP_201_CREATED)
async def predict(input_data : features):
    
    df = pd.DataFrame([input_data.model_dump()])
    
    prediction = gradient.predict_proba(df)
    prediction_class = gradient.predict(df)
    result = 'Positive' if prediction_class[0] == 1 else 'Negative'
   
    return {
        'prediction' : prediction.tolist(),
        'results': result
    }


@app.post('/predict_sepsis')
def predict_sepsis(data: features, model: str = Query('random_forest', enum=['random_forest', 'gradient'])):
    df = pd.DataFrame([data.model_dump()])
 
    # Select the model based on the query parameter
    if model == 'random_forest':
        prediction = random_forest.predict(df)
        probability = random_forest.predict_proba(df)
    elif model == 'gradient':
        prediction = gradient.predict(df)
        probability = gradient.predict_proba(df)
   
    prediction = int(prediction[0])
    prediction = encoder.inverse_transform([prediction])[0]
    probability = probability[0]
 
    return {
        'model_used': model,
        'prediction': prediction,
        'probability': f'The probability of the prediction is {probability[0]:.2f}'
    }