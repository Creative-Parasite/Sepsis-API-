from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

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

# Load the trained model
# @app.get('/trained_models')
# def load_gradient():
#     gradient = joblib.load("toolkit/GradientBoostingClassifier.joblib")
#     return gradient
# @app.post('/train')
# def load_random():
#     forest = joblib.load("toolkit/random_forest.joblib")
#     return forest

pipeline = joblib.load('./toolkit/GradientBoostingClassifier.joblib')

@app.post('/prediction')
async def predict(input_data : features):
    
    df = pd.DataFrame([input_data.model_dump()])
    
    # if input_data.model == 'gradient':
    #     prediction = load_gradient.predict_proba(df)
    # else: 
    #     prediction = load_random.predict_proba(df)
        
    encoder = joblib.load("toolkit/label_encoder.joblib")
    prediction = int(prediction[0])
    # prediction_class = encoder.inverse_transform(prediction)
    # result = 'Positive' if prediction_class[0] == 'Positive' else 'Negative'
    
    return {
        "data" : input,
        # 'prediction_class' : prediction_class.to_list(),
        'prediction' : prediction.to_list(),
         }
    
    