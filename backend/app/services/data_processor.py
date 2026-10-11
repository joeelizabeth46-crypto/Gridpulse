from .weather_service import get_current_weather
from .solar_services import get_solar_position


def get_environmental_data(latitude, longitude):
    """
    Combine current weather data and solar data
    for a given geographical location.
    """

    weather = get_current_weather(latitude, longitude)
    solar = get_solar_position(latitude, longitude)

    return {
        "location": {
            "latitude": latitude,
            "longitude": longitude
        },
        "weather": weather,
        "solar": solar
    }