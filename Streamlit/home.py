import streamlit as st
import pandas as pd 
import requests

# backend_url = "http://localhost:8000"

backend_url ="http://backend:80"

st.set_page_config(
    page_title= 'SEPSIS API',
    page_icon= "house_icon.png",
    layout='wide'
)

def main():
    st.title('SEPSIS API')
    st.markdown("""
         Sepsis also known as **Blood poisoning** -
         An integration of API for detecting Sepsis on patients in the ICU. 
         """
          )
    with st.form('input-feature'):
        st.subheader('Sepsis Input Features')
        col1, col2, = st.columns(2)
        with col1:
            prg = st.number_input('Plasma glucose levels', min_value=0, step=1)
            pl = st.number_input('Blood work results 1', min_value=0, step=1)
            pr = st.number_input('Blood pressure', min_value=0, step=1)
            sk = st.number_input('Blood work results 2', min_value=0, step=1)
        with col2:
            ts = st.number_input('Blood work results 3', min_value=0, step=1)
            m11 = st.number_input('Body mass index', min_value=0, step=1)
            bd2 = st.number_input('Blood work results 4', min_value=0, step=1)
            age = st.number_input('Age', min_value=21, step=1)
            insurance = st.radio('Insurance', options=['Yes', 'No'])
            
        submit_button = st.form_submit_button('Predict')
        
        if submit_button:
            input_data = {
                'prg': prg,
                'pl': pl,
                'pr': pr,
                'sk': sk,
                'ts': ts,
                'm11': m11,
                'bd2': bd2,
                'age': age,
                'insurance': insurance
            }
            
            status_code = requests.get(backend_url).status_code
            
            if status_code == 200:
                response = requests.post(f"{backend_url}/predict_sepsis", json=input_data, timeout=60)
            # if response.status_code == 200:
                prediction = response.json()['prediction']
                st.success(f'The patient tested {prediction} for sepsis')
            else:
                st.error(f'Error: {response.json()["detail"]}')
        
if __name__ == '__main__':
    main()
