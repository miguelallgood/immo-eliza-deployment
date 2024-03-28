import streamlit as st
import requests
import sys
import os
import googlemaps
from googlemaps.exceptions import ApiError

# Add parent directory of predict.py to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from predict import Item

def get_coordinates(address):
    # Initialize Google Maps client with your API key
    gmaps = googlemaps.Client(key='AIzaSyAJ0AgQUHhBEldIDUrwxrS_k4RJrSnHZz4')

    try:
        # Geocode the address to retrieve latitude and longitude
        geocode_result = gmaps.geocode(address)

        if geocode_result:
            # Extract latitude and longitude from the geocode result
            location = geocode_result[0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            return latitude, longitude
        else:
            st.error("No geocode result found for the address.")
            return None, None

    except ApiError as e:
        st.error(f"Error occurred: {e}")
        return None, None

st.title('House Price Prediction')

st.write('Enter the full address below:')
street_name = st.text_input('Street Name')
property_number = st.text_input('Property Number')
postcode = st.text_input('Postcode')

if st.button('Get Latitude and Longitude'):
    # Construct full address
    address = f'{property_number} {street_name}, {postcode}'
    # Get latitude and longitude using Google Maps Geocoding API
    latitude, longitude = get_coordinates(address)
    if latitude is not None and longitude is not None:
        st.success(f'Latitude: {latitude}, Longitude: {longitude}')
    else:
        st.error('Failed to retrieve latitude and longitude. Please check the address.')

st.write('Enter the features below for price prediction:')
number_rooms = st.number_input('Number of Rooms')
living_area = st.number_input('Living Area')
garden_area = st.number_input('Garden Area')
number_facades = st.number_input('Number of Facades')

if st.button('Predict Price'):
    # Create an Item object with the entered features
    item = Item(
        number_rooms=number_rooms,
        living_area=living_area,
        garden_area=garden_area,
        number_facades=number_facades,
        Longitude=longitude,
        Latitude=latitude
    )

    # Make a POST request to the FastAPI backend for price prediction
    response = requests.post('http://localhost:8000/predict/', json=item.dict())

    if response.status_code == 200:
        prediction = response.json()['prediction']
        formatted_prediction = f'{prediction:,.2f} €'  # Format prediction with 2 decimals and euro sign
        st.success(f'Predicted Price: {formatted_prediction}')
    else:
        st.error('Price prediction failed. Please try again.')
