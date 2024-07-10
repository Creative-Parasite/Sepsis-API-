import streamlit as st
import pandas as pd 
import numpy as np
import joblib
import requests
import json

st.set_page_config(
    page_title= 'SEPSIS API',
    page_icon= "house_icon.png",
    layout='wide'
)

## FAST API
response = requests.get()

models = {
    'random_forest': 'random_forest',
    'gradient_boost': 'gradient',
}

def main():
    st.title('SEPSIS API')
    
    st.write("""
         Sepsis also known as **Blood poisoning**
         An integration of API for detecting Sepsis on patients in the ICU. 
         """
          )

    ## Create a select box 
    with st.sidebar:
        selection = st.selectbox("Please select your models", list(models.key()))
        
        
    ## get models file name based on selection
    model_name = models[selection]
    
    
    ## Features 
    prg = st.number_input("Plasma glucose level")
    pl = st.number_input("Blood work results 1")
    pr = st.number_input("Blood pressure")
    sk = st.number_input("Blood work results 2")
    ts = st.number_input("Blood work results 3")
    m11 = st.number_input("Body mass index", min_value=0, step=1)
    bd2 = st.number_input("Blood work results 4")
    age = st.number_input("What is the patient's age?", min_value=0, max_value= 70, step=1)
    insurance = st.radio('Insurance', options=['Yes', 'No'])
    
    if st.button('Predict'):
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
        
        feature_data = [prg, pl, pr, sk, ts, m11,bd2, age, insurance]
        
        ## Json serialization
        # Call FastAPI endpoint and get prediction result
        headers = {'Content-Type': 'application/json'}
        response = requests.post(response + f"/{model_name}", json=feature_data)

        # Display prediction result
        st.write(f"Prediction: {response.json()}")
    
if __name__ == "__main__":
    main() 
        

