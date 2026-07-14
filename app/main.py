from fastapi import FastAPI

import app.models

from app.database import Base
from app.database import engine
from app.routers.auth import router as auth_router
from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)


@app.get("/")
def root(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "phone": current_user.phone,
    }