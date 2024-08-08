from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi_versioning import version
from db.mongodb import Users
from core.security.security import require_auth
from bson import ObjectId


router = APIRouter()


@router.get("/{userId}")
@version(1)
def get_user(userId: str, auth: dict = Depends(require_auth)):
    try:
        userId = ObjectId(userId)

        user = Users.find_one({"_id": userId}, {"password": 0})

        if user is None:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"error": f"{userId} does not exist."},
            )

        user["_id"] = str(user["_id"])
        return JSONResponse(status_code=status.HTTP_200_OK, content=user)

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": f"{str(error)}"},
        )
