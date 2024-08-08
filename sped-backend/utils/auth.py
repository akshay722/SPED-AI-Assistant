from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from utils.buildError import BuildError
from typing import Union, Any
from jose import jwt
import re
from fastapi import status
import logging

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 60 min
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30  # 30 days
ALGORITHM = os.environ.get("ALGORITHM")
JWT_SECRET_KEY = os.environ.get("SECRET_KEY")  # should be kept secret

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    try:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(
                minutes=ACCESS_TOKEN_EXPIRE_MINUTES
            )

        to_encode = {"exp": expires_delta, "userId": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
        return encoded_jwt

    except Exception as error:
        logging.error("Getting error in create access token : ", error)
        raise BuildError(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=error
        )


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    try:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(
                minutes=REFRESH_TOKEN_EXPIRE_MINUTES
            )

        to_encode = {"exp": expires_delta, "userId": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
        return encoded_jwt

    except Exception as error:
        logging.error("Getting error in create refresh token : ", error)
        raise BuildError(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=error
        )


def validate_password(password: str):
    try:

        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[~}{\[\]~!@#$%^&*()_\-+=:;\"'<>?/.,\\])[A-Za-z\d~}{\[\]~!@#$%^&*()_\-+=:;\"'<>?/.,\\]{8,12}$"

        if not re.match(pattern, password):
            return False
        else:
            return True

    except Exception as error:
        logging.error("Getting error in validate password function : ", error)
        raise BuildError(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=error
        )
