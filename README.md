# House Price Prediction App

This is a Streamlit web application for predicting apartment prices based on various features such as number of rooms, living area, garden area, and number of facades. It uses a FastAPI backend for prediction and Google Maps Geocoding API to retrieve latitude and longitude coordinates based on the provided address.

## Features

- Input the full address to retrieve latitude and longitude coordinates.
- Input features such as number of rooms, living area, garden area, and number of facades.
- Predict the price of the house based on the provided features.

## Installation

1. Clone the repository: `git clone https://github.com/miguelallgood/immo-eliza-deployment.git`
2. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Run the Streamlit app: `streamlit run streamlit_app.py`
2. Enter the desired features for price prediction and click `"Predict price"` to get the predicted price.

## Dependencies

- Streamlit
- Requests
- FastAPI

## Credits

This project was created by Miguel Bueno [https://github.com/miguelallgood]

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.






