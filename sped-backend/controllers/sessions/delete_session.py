from fastapi_versioning import version
from fastapi import APIRouter, status, Depends
from db.mongodb import Sessions
from fastapi.responses import JSONResponse
from core.security.security import require_auth

router = APIRouter()


@router.delete("/delete/{userId}/{sessionId}")
@version(1)
def delete_session(sessionId: str, userId: str, auth: dict = Depends(require_auth)):
    try:
        session = Sessions.find_one({"userId": userId, "sessionId": sessionId})

        if session is None:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"error": f"{sessionId} does not exists."},
            )

        delete_sessions = Sessions.delete_one(
            {"userId": userId, "sessionId": sessionId}
        )

        if delete_sessions.deleted_count != 0:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "Session deleted successfully."},
            )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": f"{str(error)}"},
        )
