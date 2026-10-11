
import pandas as pd

from app.services.ml_prediction_service import (
    load_ml_assets,
    predict_next_four_hours,
    FEATURE_COLUMNS,
)

CSV_PATH = "backend/data/plant1_features.csv"

df = pd.read_csv(CSV_PATH)
df["DATE_TIME"] = pd.to_datetime(df["DATE_TIME"])
df = df.sort_values("DATE_TIME").reset_index(drop=True)

# Convert required features to numeric values.
df[FEATURE_COLUMNS] = df[FEATURE_COLUMNS].apply(
    pd.to_numeric, errors="coerce"
)
df = df.dropna(subset=FEATURE_COLUMNS).reset_index(drop=True)

window = None
start_time = None

# Find 16 consecutive 15-minute records.
for i in range(len(df) - 15):
    w = df.iloc[i:i + 16]

    correct_intervals = (
        w["DATE_TIME"].diff().dropna()
        == pd.Timedelta(minutes=15)
    ).all()

    continuous_flags = w["CONTINUOUS"].iloc[1:].astype(bool).all()

    if correct_intervals and continuous_flags:
        window = w[FEATURE_COLUMNS].to_numpy(dtype=float)
        start_time = w["DATE_TIME"].iloc[0]
        break

if window is None:
    raise ValueError("No valid continuous 16-record window found.")

# Load the trained model and its original scalers.
model, feature_scaler, target_scaler = load_ml_assets()

predictions = predict_next_four_hours(
    window, model, feature_scaler, target_scaler
)

print("Historical data window:", start_time)
print("Number of input records:", len(window))
print("Prediction execution: SUCCESS")
print("Number of output predictions:", len(predictions))
print("First 3 outputs:", predictions[:3])
print(
    "Forecast timestamps would begin at:",
    start_time + pd.Timedelta(minutes=240),
)
