
from fastapi import FastAPI
from sqlalchemy import text

from backend.database import engine
from backend.database import get_db
from backend.power import router as power_router
from backend.environment import router as environment_router
from backend.forecast import router as forecast_router
from backend.weather import get_current_weather
from backend.users import router as users_router

app = FastAPI(
    title="GridPulse API",
    description="Backend API for GridPulse solar power forecasting",
    version="1.0.0"
)


app.include_router(power_router)
app.include_router(environment_router)
app.include_router(forecast_router)
app.include_router(users_router)

@app.get("/api/weather/current", tags=["Weather"])
def current_weather():
    return get_current_weather()


@app.get("/")
def root():
    return {
        "message": "GridPulse API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/health/database")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception:
        return {
            "status": "unhealthy",
            "database": "disconnected"
        }
