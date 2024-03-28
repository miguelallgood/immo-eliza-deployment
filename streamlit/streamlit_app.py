import os
import sys
import streamlit as st
import requests

# Add parent directory of predict.py to Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

# Now you can import predict module
from predict import Item

st.title('Apartment for sale')

st.write('Enter the features below:')
number_rooms = st.number_input('Number of Rooms', min_value=0)
living_area = st.number_input('Living Area (m²)', step=20)
garden_area = st.number_input('Garden Area (m²)', step=10)
number_facades = st.number_input('Number of Facades', min_value=0)
Longitude = st.number_input('Longitude', format="%.4f")
Latitude = st.number_input('Latitude', format="%.4f")

item = Item(
    number_rooms=number_rooms,
    living_area=living_area,
    garden_area=garden_area,
    number_facades=number_facades,
    Longitude=Longitude,
    Latitude=Latitude
)

if st.button('Predict'):
    # Make a POST request to your FastAPI backend
    response = requests.post('http://localhost:8000/predict/', json=item.dict())

    if response.status_code == 200:
        prediction = response.json()['prediction']
        # Format the prediction value with 2 decimals and euro sign
        # formatted_prediction = f'{prediction:.2f} €'
        # Add comma formatting
        formatted_prediction_with_commas = "{:,.2f}".format(prediction) + " €"
        st.success(f'Prediction: {formatted_prediction_with_commas}')
    else:
        st.error('Prediction failed. Please try again.')
