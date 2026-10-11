import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Find the backend/.env file reliably
BASE_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_current_weather(latitude, longitude):
    """
    Fetch current weather data from OpenWeatherMap
    using latitude and longitude.
    """

    if not API_KEY:
        raise ValueError("OPENWEATHER_API_KEY is not set in .env")

    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code != 200:
        raise Exception(
            f"OpenWeather API error: {response.status_code} - {response.text}"
        )

    data = response.json()

    rainfall = 0

    if "rain" in data:
        rainfall = data["rain"].get("1h", 0)

    return {
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "cloud_cover": data["clouds"]["all"],
        "wind_speed": data["wind"]["speed"],
        "wind_direction": data["wind"].get("deg", 0),
        "rainfall": rainfall,
        "weather_condition": data["weather"][0]["description"]
    }