from fastapi import HTTPException, status, Header
import jwt
from datetime import datetime
from utils.buildError import BuildError
from dotenv import load_dotenv
import os

load_dotenv()

secret = os.environ.get("SECRET_KEY")
algorithm = os.environ.get("ALGORITHM")


def require_auth(authorization: str = Header(None)):
    try:
        if authorization is None or not authorization.startswith("Bearer "):
            raise BuildError(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content="Token not provided.",
            )

        token = authorization.replace("Bearer ", "", 1)

        # Verify the token's signature
        decoded_token = jwt.decode(token, secret, algorithms=[algorithm])
        # user = Users.find_one({"_id": ObjectId(str(user_id))})

        # Check token expiration
        if "exp" in decoded_token:
            current_time = datetime.utcnow().timestamp()
            if current_time > decoded_token["exp"]:
                raise BuildError(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content="The token has expired. Please login in again",
                )
        return decoded_token

    except BuildError as error:
        raise HTTPException(
            status_code=error.status_code or status.HTTP_401_UNAUTHORIZED,
            detail=error.content or "Invalid token",
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The token has expired. Please login in again",
        )
