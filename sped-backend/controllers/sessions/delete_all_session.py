from fastapi_versioning import version
from fastapi import APIRouter, status, Depends
from db.mongodb import Users, Sessions
from fastapi.responses import JSONResponse
from core.security.security import require_auth
from bson.objectid import ObjectId

router = APIRouter()


@router.delete("/deleteAll/{userId}")
@version(1)
def delete_all_session(userId: str, auth: dict = Depends(require_auth)):
    try:
        user = Users.find_one({"_id": ObjectId(userId)})

        if user is None:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"error": "User does not exists."},
            )

        delete_sessions = Sessions.delete_many({"userId": userId})

        if delete_sessions.deleted_count != 0:
            print("Session deleted.")
        else:
            print("Session does not exist.")

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Session deleted successfully."},
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": f"{str(error)}"},
        )
