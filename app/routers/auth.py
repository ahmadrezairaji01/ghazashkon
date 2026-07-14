from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.auth.jwt import create_access_token
from app.database import get_db
from app.models.user import User
from app.schemas.auth import LoginRequest
from app.schemas.auth import RegisterRequest
from app.schemas.auth import TokenResponse
from app.services.auth_service import register

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register_user(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):
    user = register(db, request.phone)

    return {
        "id": user.id,
        "phone": user.phone,
    }


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(
        User.phone == request.phone
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    if request.code != "0000":
        raise HTTPException(
            status_code=401,
            detail="Invalid verification code",
        )

    token = create_access_token(user.id)

    return {
        "access_token": token,
    }