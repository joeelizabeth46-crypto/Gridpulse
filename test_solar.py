from app.services.solar_services import get_solar_position


# Kottayam, Kerala
latitude = 9.5916
longitude = 76.5222

try:
    solar = get_solar_position(latitude, longitude)

    print("================================")
    print("   GRIDPULSE SOLAR TEST")
    print("================================")
    print(f"Solar Elevation        : {solar['solar_elevation']}°")
    print(f"Solar Azimuth          : {solar['solar_azimuth']}°")
    print(f"Solar Zenith           : {solar['solar_zenith']}°")
    print(f"Sunrise                : {solar['sunrise']}")
    print(f"Sunset                 : {solar['sunset']}")
    print(
        f"Daylight Duration      : "
        f"{solar['daylight_duration_hours']} hours"
    )
    print("--------------------------------")
    print("pvlib solar calculation: OK")
    print("================================")

except Exception as e:
    print("================================")
    print("   SOLAR TEST FAILED")
    print("================================")
    print(f"Error: {e}")