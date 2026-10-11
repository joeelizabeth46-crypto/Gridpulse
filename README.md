
# GridPulse

GridPulse is a solar power forecasting project that integrates weather data, solar calculations, and machine learning predictions.

## Technologies

- Python
- FastAPI
- OpenWeatherMap API
- pvlib
- Pandas and NumPy
- TensorFlow and scikit-learn

## Backend Setup

1. Install Python.
2. Create and activate a virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create `backend/.env` using `backend/.env.example`.
5. Add your OpenWeatherMap API key to `backend/.env`.

## Run the Backend

From the project root, run:

```bash
python -m uvicorn app.main:app --reload --app-dir backend
```

Open the API documentation:

http://127.0.0.1:8000/docs

## Main API Endpoints

- `/api/weather`
- `/api/solar-position`
- `/api/environmental-data`
- `/api/historical-prediction`
- `/api/gridpulse-forecast`
