from pydantic import BaseModel


class RegisterRequest(BaseModel):
    phone: str


class LoginRequest(BaseModel):
    phone: str
    code: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"