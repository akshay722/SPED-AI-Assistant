from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from utils.auth import create_access_token, create_refresh_token, verify_password
from db.mongodb import Users
from models.auth import Login
from fastapi_versioning import version

router = APIRouter()


@router.post("/login")
@version(1)
async def login(request: Login):
    try:
        user = Users.find_one({"email": request.email})
        if user is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"error": "User is not Found"},
            )

        hashed_pass = user["password"]
        if not verify_password(request.password, hashed_pass):
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={"error": "Incorrect password"},
            )

        user["_id"] = str(user["_id"])
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "access_token": create_access_token(str(user["_id"])),
                "user": user,
                "refresh_token": create_refresh_token(str(user["_id"])),
            },
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
