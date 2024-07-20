from fastapi import FastAPI,status
from typing import Union
import joblib
import pandas as pd
from pydantic import BaseModel
import streamlit as st 
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "HELLO WORLD!"}


@app.get("/show")
def show(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

## Load your models and encoder
gradient = joblib.load("../models/toolkit/GradientBoostingClassifier.joblib")
random_forest = joblib.load("../models/toolkit/random_forest.joblib")
encoder = joblib.load("../models/toolkit/label_encoder.joblib")

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import joblib
import pandas as pd

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
    
    
class PredictionInput(BaseModel):
    inputs: list[features]
    # model: str

@app.post("/predict")
async def predict(input_data: PredictionInput):
    input_df = pd.DataFrame(input_data.inputs)
    
    prediction = gradient.predict_proba(input_df)
    
    # if input_data.model == "gradient":
    #     prediction = gradient.predict_proba(input_df)
    # elif input_data.model == "random_forest":
    #     prediction = random_forest.predict_proba(input_df)
    # else:
    #     return JSONResponse(status_code=400, content={"error": "Invalid model choice"})
    
    return {"prediction": prediction.tolist()}
    
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
## FAST API
API_url= "http://127.0.0.1:8000/"


def main():
    
    st.title('SEPSIS API')
    
    st.write("""
         Sepsis also known as **Blood poisoning**
         An integration of API for detecting Sepsis on patients in the ICU. 
         """
          )

    with st.form('input-data'):
        st.subheader("Sepsis fetures")
        ## Features 
        prg = st.number_input("Plasma glucose level", min_value= 0)
        pl = st.number_input("Blood work results 1", min_value=0)
        pr = st.number_input("Blood pressure", min_value=0)
        sk = st.number_input("Blood work results 2")
        ts = st.number_input("Blood work results 3")
        m11 = st.number_input("Body mass index", min_value=0, step=1)
        bd2 = st.number_input("Blood work results 4")
        age = st.number_input("What is the patient's age?", min_value=0, max_value= 70, step=1)
        insurance = st.radio('Insurance', options=['Yes', 'No'], key='insurance')
        
        submit_button = st.form_submit_button('Predict')
        
        if submit_button:
            ## Prepare feature data as JSON payload
            feature_data= {
                'prg': prg,
                'pl': pl,
                'pr': pr,
                'sk': sk,
                'ts': ts,
                'm11': m11,
                'bd2': bd2,
                'Age': age,
                'Insurance': insurance
                }
            
            ## Json serialization
            # Call FastAPI endpoint and get prediction result
            response = requests.post(f"{API_url}/predict_sepsis", json=feature_data)
            
            if response.status_code == 200:
                prediction = response.json()["prediction"]
                st.success(f" The probability of prediction {prediction}")
            else :
                st.error(f'Error: {response.json()["detail"]}')

if __name__ == "__main__":
    main()
    st.write(st.session_state)
        
