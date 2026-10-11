
import numpy as np
import pandas as pd


TIMEZONE = "Asia/Kolkata"


def add_time_features(
    df: pd.DataFrame,
    timestamp_col: str = "timestamp"
) -> pd.DataFrame:
    """
    Add cyclic time features to historical readings.

    Expected timestamp format: ISO 8601 with a timezone offset,
    for example 2026-10-10T08:00:00+05:30.

    Returns a copy of the DataFrame with four time features.
    """
    if timestamp_col not in df.columns:
        raise ValueError(
            f"Missing timestamp column: {timestamp_col}"
        )

    result = df.copy()

    # Convert timestamps to a consistent timezone.
    timestamps = pd.to_datetime(
        result[timestamp_col],
        errors="raise",
        utc=True
    ).dt.tz_convert(TIMEZONE)

    # Fractional hour includes minutes and seconds.
    hour = (
        timestamps.dt.hour
        + timestamps.dt.minute / 60
        + timestamps.dt.second / 3600
    )

    # Use the actual number of days in each year.
    day = timestamps.dt.dayofyear - 1
    days_in_year = np.where(
        timestamps.dt.is_leap_year, 366, 365
    )

    result["hour_sin"] = np.sin(2 * np.pi * hour / 24)
    result["hour_cos"] = np.cos(2 * np.pi * hour / 24)

    result["day_of_year_sin"] = np.sin(
        2 * np.pi * day / days_in_year
    )
    result["day_of_year_cos"] = np.cos(
        2 * np.pi * day / days_in_year
    )

    return result


ML_FEATURE_COLUMNS = [
    "AC_POWER",
    "AMBIENT_TEMPERATURE",
    "MODULE_TEMPERATURE",
    "IRRADIATION",
    "solar_elevation",
    "solar_azimuth",
    "hour_sin",
    "hour_cos",
    "day_of_year_sin",
    "day_of_year_cos",
]


def prepare_ml_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Arrange historical data in the exact feature order
    required by Member 1's CNN-LSTM model.

    Missing measurements are preserved, not replaced with zero.
    """
    missing_columns = [
        col for col in ML_FEATURE_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required ML columns: {missing_columns}"
        )

    result = df[ML_FEATURE_COLUMNS].copy()

    for column in ML_FEATURE_COLUMNS:
        result[column] = pd.to_numeric(
            result[column], errors="raise"
        )

    return result
