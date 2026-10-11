
import pandas as pd

from app.services.ml_features import (
    ML_FEATURE_COLUMNS,
    prepare_ml_features,
)

sample = pd.DataFrame({
    "AC_POWER": [120.0],
    "AMBIENT_TEMPERATURE": [28.0],
    "MODULE_TEMPERATURE": [None],
    "IRRADIATION": [None],
    "solar_elevation": [35.0],
    "solar_azimuth": [145.0],
    "hour_sin": [0.5],
    "hour_cos": [0.866],
    "day_of_year_sin": [0.9],
    "day_of_year_cos": [0.4],
})

result = prepare_ml_features(sample)

assert result.columns.tolist() == ML_FEATURE_COLUMNS
assert pd.isna(result.loc[0, "MODULE_TEMPERATURE"])
assert pd.isna(result.loc[0, "IRRADIATION"])

print(result.to_string(index=False))
print("\nML feature mapping test: OK")
