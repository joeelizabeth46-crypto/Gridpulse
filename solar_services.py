import pandas as pd
import pvlib


def get_solar_position(latitude, longitude, timestamp=None):
    """
    Calculate solar position, sunrise, sunset,
    and daylight duration using pvlib.
    """

    timezone = "Asia/Kolkata"

    # Use current time if no timestamp is provided
    if timestamp is None:
        timestamp = pd.Timestamp.now(tz=timezone)

    # Make timestamp timezone-aware
    if timestamp.tzinfo is None:
        timestamp = timestamp.tz_localize(timezone)
    else:
        timestamp = timestamp.tz_convert(timezone)

    # -------------------------------------------------
    # 1. Solar position
    # -------------------------------------------------

    solar_position = pvlib.solarposition.get_solarposition(
        time=timestamp,
        latitude=latitude,
        longitude=longitude
    )

    solar_elevation = float(solar_position["elevation"].iloc[0])
    solar_azimuth = float(solar_position["azimuth"].iloc[0])
    solar_zenith = float(solar_position["zenith"].iloc[0])

    # -------------------------------------------------
    # 2. Sunrise and sunset
    # -------------------------------------------------

    location = pvlib.location.Location(
        latitude=latitude,
        longitude=longitude,
        tz=timezone
    )

    # Start of the current day
    day_start = pd.DatetimeIndex(
        [timestamp.normalize()]
    )

    sun_times = location.get_sun_rise_set_transit(
        day_start
    )

    sunrise = sun_times["sunrise"].iloc[0]
    sunset = sun_times["sunset"].iloc[0]

    # -------------------------------------------------
    # 3. Daylight duration
    # -------------------------------------------------

    daylight_duration = sunset - sunrise
    daylight_hours = daylight_duration.total_seconds() / 3600

    # -------------------------------------------------
    # Return results
    # -------------------------------------------------

    return {
        "solar_elevation": round(solar_elevation, 2),
        "solar_azimuth": round(solar_azimuth, 2),
        "solar_zenith": round(solar_zenith, 2),
        "sunrise": sunrise.strftime("%H:%M:%S"),
        "sunset": sunset.strftime("%H:%M:%S"),
        "daylight_duration_hours": round(daylight_hours, 2)
    }