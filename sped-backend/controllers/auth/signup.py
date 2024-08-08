from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from models.auth import Signup
from db.mongodb import Users
from utils.auth import get_hashed_password, validate_password
from fastapi_versioning import version

router = APIRouter()


@router.post("/signup")
@version(1)
async def create_user(request: Signup):
    try:
        # validate password
        if not validate_password(request.password):
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error": "Password must be 8 to 12 characters long and contain at least one uppercase letter, one lowercase letter, and one special character."
                },
            )

        else:
            # querying database to check if user already exist
            user = Users.find_one({"email": request.email})
            if user is not None:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={"error": "User already exist."},
                )
            user_data = {
                "userName": request.userName,
                "email": request.email,
                "password": get_hashed_password(request.password),
            }
            user_data = Users.insert_one(user_data)
            insert_id = str(user_data.inserted_id)
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content={"_id": insert_id, "success": True},
            )

    except Exception as error:
        code = (
            error.status_code
            if hasattr(error, "status_code")
            else status.HTTP_422_UNPROCESSABLE_ENTITY
        )
        message = error.content if hasattr(error, "content") else str(error)

        return JSONResponse(
            status_code=code,
            content={"error": f"{message}"},
        )
