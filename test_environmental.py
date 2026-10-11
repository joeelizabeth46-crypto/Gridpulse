from app.services.data_processor import get_environmental_data


# Kottayam, Kerala
latitude = 9.5916
longitude = 76.5222

try:
    data = get_environmental_data(latitude, longitude)

    print("========================================")
    print("     GRIDPULSE ENVIRONMENTAL TEST")
    print("========================================")

    print("\nLOCATION")
    print("----------------------------------------")
    print(f"Latitude        : {data['location']['latitude']}")
    print(f"Longitude       : {data['location']['longitude']}")

    print("\nWEATHER")
    print("----------------------------------------")
    weather = data["weather"]

    print(f"Temperature     : {weather['temperature']} °C")
    print(f"Feels Like      : {weather['feels_like']} °C")
    print(f"Humidity        : {weather['humidity']} %")
    print(f"Pressure        : {weather['pressure']} hPa")
    print(f"Cloud Cover     : {weather['cloud_cover']} %")
    print(f"Wind Speed      : {weather['wind_speed']} m/s")
    print(f"Wind Direction   : {weather['wind_direction']}°")
    print(f"Rainfall        : {weather['rainfall']} mm")
    print(f"Condition       : {weather['weather_condition']}")

    print("\nSOLAR")
    print("----------------------------------------")
    solar = data["solar"]

    print(f"Solar Elevation : {solar['solar_elevation']}°")
    print(f"Solar Azimuth   : {solar['solar_azimuth']}°")
    print(f"Solar Zenith    : {solar['solar_zenith']}°")
    print(f"Sunrise         : {solar['sunrise']}")
    print(f"Sunset          : {solar['sunset']}")
    print(
        f"Daylight        : "
        f"{solar['daylight_duration_hours']} hours"
    )

    print("\n----------------------------------------")
    print("Environmental data combination: OK")
    print("========================================")

except Exception as e:
    print("========================================")
    print("   ENVIRONMENTAL TEST FAILED")
    print("========================================")
    print(f"Error: {e}")