from fastapi import FastAPI, HTTPException, status, Query
import joblib
from pydantic import BaseModel
import pandas as pd
import logging


Description = """
 This API predicts the presence of Sepsis based on the provided features.
 The API supports two models: Gradient Boosting Classifier and Random Forest Classifier.
 Both models are trained on a dataset from the UCI Machine Learning Repository.

 FEATURES
 
    "prg": Plasma glucose level,
    "pl": Blood work results 1 <mu U/ml>,
    "pr": Blood pressure <mm hg>,
    "sk": Blood work results 2  <mm>,
    "ts": Blood work results 3 <mu U/ml>,
    "m11": Body mass index <weight in kg / height in m^2>,
    "bd2": Blood work results 4 <mu U/ml>,
    "age": Patient's age ,
    "insurance": Presence of an insurance card or not"
 

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
    
    
@app.get('/')
def get_sepsis():
    return {'Title': 'Sepsis prediction API'}


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