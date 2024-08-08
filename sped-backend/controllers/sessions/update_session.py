from fastapi import APIRouter, status, Body
from fastapi_versioning import version
from db.mongodb import Sessions
from fastapi.responses import JSONResponse
import json
import datetime

from models.sessions import updateSession

router = APIRouter()


@router.patch("/{userId}/{sessionId}")
@version(1)
def update_session(userId: str, sessionId: str, request: updateSession):
    try:
        session = Sessions.find_one_and_update(
            {"userId": userId, "sessionId": sessionId},
            {
                "$set": {
                    "sessionName": request.sessionName,
                    "updatedAt": datetime.datetime.utcnow(),
                }
            },
            {"done": True},
        )

        if session is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"error": "Session does not exist."},
            )

        session["_id"] = str(session["_id"])

        return JSONResponse(status_code=status.HTTP_200_OK, content=session)

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": f"{str(error)}"},
        )
