
import pandas as pd

from app.services.ml_features import add_time_features


sample_data = pd.DataFrame({
    "timestamp": [
        "2026-10-10T06:00:00+05:30",
        "2026-10-10T06:15:00+05:30",
        "2026-10-10T12:00:00+05:30",
        "2026-10-10T18:00:00+05:30",
    ]
})

result = add_time_features(sample_data)

print("\nTIME FEATURES")
print(result.to_string(index=False))

required_columns = [
    "hour_sin",
    "hour_cos",
    "day_of_year_sin",
    "day_of_year_cos",
]

assert all(col in result.columns for col in required_columns)
assert result[required_columns].notna().all().all()

print("\nML time-feature test: OK")
