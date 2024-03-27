import streamlit as st
import requests
from predict import Item

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
    # response = requests.post('http://localhost:8000/predict/', json=item.dict())
    response = requests.post('https://immo-eliza-deployment-h5ai.onrender.com', json=item.dict())

    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.success(f'Prediction: {prediction}')
    else:
        st.error('Prediction failed. Please try again.')
