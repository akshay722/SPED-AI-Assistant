from fastapi import Depends, APIRouter, status, Header, Path
from fastapi.responses import JSONResponse
from core.security.security import require_auth
from db.mongodb import Sessions
from fastapi_versioning import version
import json

router = APIRouter()


@router.get("/getSession/{userId}/{sessionId}")
@version(1)
def get_session(userId: str, sessionId: str, auth: dict = Depends(require_auth)):
    try:
        session_data = Sessions.find_one({"userId": userId, "sessionId": sessionId})

        if not session_data:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"error": "Session does not exist."},
            )
        else:
            session_data["_id"] = str(session_data["_id"])
            session_data["createdAt"] = str(session_data["createdAt"])
            session_data["updatedAt"] = str(session_data["updatedAt"])

            return JSONResponse(status_code=status.HTTP_200_OK, content=session_data)

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": f"{str(error)}"},
        )
