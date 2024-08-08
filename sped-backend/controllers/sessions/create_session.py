import datetime
from typing import Annotated
from bson import ObjectId
from fastapi import Depends, APIRouter, Query, status, Body
from fastapi.responses import JSONResponse
from core.security.security import require_auth
from db.mongodb import Sessions, Users
from fastapi_versioning import version
import uuid
import requests

from models.sessions import createSession


router = APIRouter()


@router.post("/createSession")
@version(1)
def create_session(
    request: createSession,
    isPrivate: bool = Query(...),
    auth: dict = Depends(require_auth),
):
    try:

        user = Users.find_one({"_id": ObjectId(request.userId)})

        if not user:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"error": "User does not exist."},
            )

        # Generate a random session ID
        sessionId = str(uuid.uuid4())

        value = {
            "sessionId": sessionId,
            "sessionName": "Untitled",
            "userId": request.userId,
            "description": "",
            "isPrivate": isPrivate,
            "createdAt": datetime.datetime.utcnow(),
            "updatedAt": datetime.datetime.utcnow(),
        }

        # Insert sessionId in collection
        session = Sessions.insert_one(value)

        value["_id"] = str(value["_id"])
        value["createdAt"] = str(value["createdAt"])
        value["updatedAt"] = str(value["updatedAt"])

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=value,
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": f"{str(error)}"},
        )
