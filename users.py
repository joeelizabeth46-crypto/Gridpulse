from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.auth import hash_password, verify_password, create_access_token
from backend.schemas import UserRegister, UserResponse
from backend.schemas import UserRegister, UserResponse, UserLogin

router = APIRouter(
    prefix="/api",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    # Check whether the email is already registered
    existing_user = db.execute(
        text("""
            SELECT user_id
            FROM users
            WHERE email = :email
        """),
        {"email": user.email}
    ).mappings().first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists."
        )

    # Hash the password before storing it
    password_hash = hash_password(user.password)

    try:
        result = db.execute(
            text("""
                INSERT INTO users (
                    name,
                    email,
                    password_hash,
                    phone
                )
                VALUES (
                    :name,
                    :email,
                    :password_hash,
                    :phone
                )
                RETURNING user_id, name, email, phone
            """),
            {
                "name": user.name,
                "email": user.email,
                "password_hash": password_hash,
                "phone": user.phone
            }
        )

        new_user = dict(result.mappings().one())
        db.commit()

        return new_user

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration failed."
        )

from backend.auth import verify_password
from backend.schemas import UserLogin


@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    result = db.execute(
        text("""
            SELECT user_id, name, email, phone, password_hash
            FROM users
            WHERE email = :email
        """),
        {"email": user.email}
    ).mappings().first()

    if not result or not verify_password(
        user.password,
        result["password_hash"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )

    return {
        "status": "success",
        "message": "Login successful.",
        "user": {
            "user_id": result["user_id"],
            "name": result["name"],
            "email": result["email"],
            "phone": result["phone"]
        }
    }