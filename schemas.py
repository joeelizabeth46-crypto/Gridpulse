from pydantic import BaseModel, EmailStr, Field


# Forecast schemas
class ForecastRequest(BaseModel):
    latitude: float
    longitude: float


class ForecastResponse(BaseModel):
    latitude: float
    longitude: float
    forecast_hours: int
    status: str
    message: str


# User registration schema
class UserRegister(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=72)
    phone: str | None = Field(default=None, max_length=20)


# User login schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1, max_length=72)


# User response schema (never returns the password hash)
class UserResponse(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    phone: str | None = None
