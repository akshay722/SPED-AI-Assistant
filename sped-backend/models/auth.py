from pydantic import BaseModel, EmailStr


class Signup(BaseModel):
    userName: str
    email: EmailStr
    password: str
    # cPassword: str


class Login(BaseModel):
    email: EmailStr
    password: str
