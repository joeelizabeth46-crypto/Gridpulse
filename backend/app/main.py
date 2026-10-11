from fastapi import FastAPI
from app.services.weather_service import get_current_weather
from app.services.solar_services import get_solar_position
from app.services.data_processor import get_environmental_data

from app.services.historical_prediction_service import (
    get_historical_prediction,
)
app = FastAPI(title="GridPulse API")


@app.get("/")
def home():
    return {
        "message": "GridPulse API is running"
    }


@app.get("/api/weather")
def weather(latitude: float, longitude: float):
    return get_current_weather(latitude, longitude)

@app.get("/api/solar-position")
def solar_position(latitude: float, longitude: float):
    return get_solar_position(latitude, longitude)

@app.get("/api/environmental-data")
def environmental_data(latitude: float, longitude: float):
    return get_environmental_data(latitude, longitude)

@app.get("/api/historical-prediction")
def historical_prediction():
    return get_historical_prediction()

@app.get("/api/gridpulse-forecast")
def gridpulse_forecast(latitude: float, longitude: float):
    environmental_data = get_environmental_data(
        latitude, longitude
    )

    prediction_data = get_historical_prediction()

    return {
        "location": environmental_data["location"],
        "weather": environmental_data["weather"],
        "solar": environmental_data["solar"],
        "prediction": prediction_data,
    }