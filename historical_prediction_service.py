
from pathlib import Path

import pandas as pd

from app.services.ml_prediction_service import (
    FEATURE_COLUMNS,
    load_ml_assets,
    predict_next_four_hours,
)

CSV_PATH = Path(__file__).resolve().parents[2] / "data" / "plant1_features.csv"


def get_historical_prediction():
    if not CSV_PATH.is_file():
        raise FileNotFoundError(
            f"Historical dataset not found: {CSV_PATH}"
        )

    df = pd.read_csv(CSV_PATH)

    required_columns = ["DATE_TIME", "CONTINUOUS"] + FEATURE_COLUMNS
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["DATE_TIME"] = pd.to_datetime(
        df["DATE_TIME"], errors="coerce"
    )
    df = df.dropna(subset=["DATE_TIME"])
    df = df.sort_values("DATE_TIME").reset_index(drop=True)

    df[FEATURE_COLUMNS] = df[FEATURE_COLUMNS].apply(
        pd.to_numeric, errors="coerce"
    )

    window = None
    start_time = None

    for i in range(len(df) - 15):
        rows = df.iloc[i:i + 16]

        if rows[FEATURE_COLUMNS].isna().any().any():
            continue

        intervals = rows["DATE_TIME"].diff().dropna()
        if not (intervals == pd.Timedelta(minutes=15)).all():
            continue

        flags = rows["CONTINUOUS"].iloc[1:]
        if not flags.map(
            lambda value: str(value).strip().lower() == "true"
        ).all():
            continue

        window = rows[FEATURE_COLUMNS].to_numpy(dtype=float)
        start_time = rows["DATE_TIME"].iloc[-1]
        break

    if window is None:
        raise ValueError("No valid 16-record historical window found.")

    model, feature_scaler, target_scaler = load_ml_assets()

    predictions = predict_next_four_hours(
        window, model, feature_scaler, target_scaler
    )
    # Solar power cannot be negative.
    predictions = [max(0.0, float(value)) for value in predictions]

    forecast_start = start_time + pd.Timedelta(minutes=15)

    return {
        "data_source": "historical_training_dataset",
        "is_live_forecast": False,
        "input_records": 16,
        "forecast_interval_minutes": 15,
        "forecast_start": forecast_start.isoformat(),
        "predictions": [
            {
                "timestamp": (
                    forecast_start
                    + pd.Timedelta(minutes=15 * i)
                ).isoformat(),
                "predicted_ac_power": float(value),
            }
            for i, value in enumerate(predictions)
        ],
        "note": (
            "Demonstration using historical training data; "
            "not a forecast for current conditions."
        ),
    }
