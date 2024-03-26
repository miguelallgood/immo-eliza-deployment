import joblib
from sklearn.preprocessing import StandardScaler
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    number_rooms: float
    living_area: float
    garden_area: float
    number_facades: float
    Longitude: float
    Latitude: float

def predict(item: Item) -> Optional[float]:
    model = joblib.load('api/new_best_model.pkl')  # Load your trained model
    scaler = joblib.load('api/new_input_scaler.pkl')  # Load your stored scaler
    input_data = [[item.number_rooms, item.living_area, item.garden_area, item.number_facades, item.Longitude, item.Latitude]]
    input_data_scaled = scaler.transform(input_data)
    prediction_scaled = model.predict(input_data_scaled)
    price_scaler = joblib.load('api/new_target_scaler.pkl')  # Load the scaler used for 'price' during training
    prediction = price_scaler.inverse_transform(prediction_scaled.reshape(-1, 1))
    return prediction[0][0] if prediction else None
