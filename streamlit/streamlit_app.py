import os
import sys
import streamlit as st
import requests
import logging

# Add parent directory of predict.py to Python path
predict_module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(predict_module_path)

from predict import Item

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.title('House Price Prediction')

st.write('Enter the features below:')
number_rooms = st.number_input('Number of Rooms')
living_area = st.number_input('Living Area')
garden_area = st.number_input('Garden Area')
number_facades = st.number_input('Number of Facades')
Longitude = st.number_input('Longitude')
Latitude = st.number_input('Latitude')

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
        formatted_prediction = "{:,.2f} €".format(prediction)  # Format prediction with comma and 2 decimals
        st.success(f'Prediction: {formatted_prediction}')
        logger.info('Prediction successful')
    else:
        st.error('Prediction failed. Please try again.')
        logger.error('Prediction failed')
