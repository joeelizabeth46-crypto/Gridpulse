from app.services.weather_service import get_current_weather


# Sample location: Kottayam, Kerala
latitude = 9.5916
longitude = 76.5222

try:
    weather = get_current_weather(latitude, longitude)

    print("================================")
    print("   GRIDPULSE WEATHER TEST")
    print("================================")
    print(f"Temperature   : {weather['temperature']} °C")
    print(f"Feels Like    : {weather['feels_like']} °C")
    print(f"Humidity      : {weather['humidity']} %")
    print(f"Pressure      : {weather['pressure']} hPa")
    print(f"Cloud Cover   : {weather['cloud_cover']} %")
    print(f"Wind Speed    : {weather['wind_speed']} m/s")
    print(f"Wind Direction: {weather['wind_direction']}°")
    print(f"Rainfall      : {weather['rainfall']} mm")
    print(f"Condition     : {weather['weather_condition']}")
    print("--------------------------------")
    print("OpenWeatherMap connection: OK")
    print("================================")

except Exception as e:
    print("================================")
    print("   WEATHER TEST FAILED")
    print("================================")
    print(f"Error: {e}")