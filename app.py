import streamlit as st
import pandas as pd
from joblib import load

# Load model
model = load("model.joblib")

st.set_page_config(page_title="🏡 House Price Predictor", page_icon="💰")
st.title("🏡 House Price Prediction App")
st.markdown("Enter the property details below:")

# Input fields
income = st.number_input("Average Area Income ($)", value=50000.0, step=1000.0)
house_age = st.number_input("Average Area House Age (years)", value=5.0)
rooms = st.number_input("Average Area Number of Rooms", value=5.0)
bedrooms = st.number_input("Average Area Number of Bedrooms", value=3.0)
population = st.number_input("Area Population", value=30000.0)

if st.button("Predict Price"):
    input_df = pd.DataFrame({
        'Avg. Area Income': [income],
        'Avg. Area House Age': [house_age],
        'Avg. Area Number of Rooms': [rooms],
        'Avg. Area Number of Bedrooms': [bedrooms],
        'Area Population': [population]
    })
    
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated House Price: ${prediction:,.2f}")
