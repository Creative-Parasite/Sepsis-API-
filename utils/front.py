import streamlit as st
import requests

backend_url = "http://127.0.0.1:8000"

# Page configuration
st.set_page_config(
    page_title='Sepsis Prediction',
    page_icon='🚀',
    layout='wide'
)

 

def show_form():
    st.header('Input Features')
    with st.form('input-feature'):
        st.subheader('Sepsis Input Features')
        col1, col2, col3 = st.columns(3)
        with col1:
            prg = st.number_input('PRG', min_value=0, step=1)
            pl = st.number_input('PL', min_value=0, step=1)
            pr = st.number_input('PR', min_value=0, step=1)
        with col2:
            sk = st.number_input('SK', min_value=0, step=1)
            ts = st.number_input('TS', min_value=0, step=1)
            m11 = st.number_input('M11', min_value=0, step=1)
        with col3:
            bd2 = st.number_input('BD2', min_value=0, step=1)
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
            
            response = requests.post(f"{backend_url}/predict_sepsis", json=input_data)
            
            if response.status_code == 200:
                prediction = response.json()['prediction']
                st.success(f'The patient tested {prediction} for sepsis')
            else:
                st.error(f'Error: {response.json()["detail"]}')
        
if __name__ == '__main__':
    show_form()