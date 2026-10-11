
from pathlib import Path

import joblib
import numpy as np
import tensorflow as tf


# Model assets stored in GridPulse/backend/ml_models
MODEL_DIR = Path(__file__).resolve().parents[2] / "ml_models"

FEATURE_COLUMNS = [
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

LOOKBACK = 16
HORIZON = 16


def load_ml_assets():
    """Load the trained model and the scalers fitted by Member 1."""
    model_path = MODEL_DIR / "best_cnn_lstm.keras"
    feature_scaler_path = MODEL_DIR / "feature_scaler.pkl"
    target_scaler_path = MODEL_DIR / "target_scaler.pkl"

    for path in (
        model_path,
        feature_scaler_path,
        target_scaler_path,
    ):
        if not path.is_file():
            raise FileNotFoundError(
                f"Required ML asset not found: {path}"
            )

    model = tf.keras.models.load_model(model_path)
    feature_scaler = joblib.load(feature_scaler_path)
    target_scaler = joblib.load(target_scaler_path)

    if model.input_shape[1:] != (LOOKBACK, len(FEATURE_COLUMNS)):
        raise ValueError(
            f"Unexpected model input shape: {model.input_shape}"
        )

    if model.output_shape[-1] != HORIZON:
        raise ValueError(
            f"Unexpected model output shape: {model.output_shape}"
        )

    if feature_scaler.n_features_in_ != len(FEATURE_COLUMNS):
        raise ValueError("Feature scaler has an unexpected feature count.")

    if target_scaler.n_features_in_ != 1:
        raise ValueError("Target scaler must accept one feature.")

    return model, feature_scaler, target_scaler


def predict_next_four_hours(
    historical_features,
    model,
    feature_scaler,
    target_scaler,
):
    """
    Predict the next 16 AC_POWER values from 16 historical rows.

    historical_features must contain exactly 16 rows and the 10
    features in FEATURE_COLUMNS order. Input values must be in the
    original, unscaled units.
    """
    values = np.asarray(historical_features, dtype=np.float64)

    expected_shape = (LOOKBACK, len(FEATURE_COLUMNS))
    if values.shape != expected_shape:
        raise ValueError(
            f"Expected input shape {expected_shape}, got {values.shape}."
        )

    if not np.isfinite(values).all():
        raise ValueError(
            "Historical features contain missing or non-finite values."
        )

    scaled = feature_scaler.transform(values)
    model_input = scaled.reshape(
        1, LOOKBACK, len(FEATURE_COLUMNS)
    )

    scaled_predictions = model.predict(
        model_input, verbose=0
    )

    if scaled_predictions.shape != (1, HORIZON):
        raise ValueError(
            f"Unexpected prediction shape: {scaled_predictions.shape}"
        )

    predictions = target_scaler.inverse_transform(
        scaled_predictions.reshape(-1, 1)
    ).ravel()

    return predictions.tolist()
