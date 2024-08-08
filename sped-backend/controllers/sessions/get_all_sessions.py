from fastapi import Query, APIRouter, status, Depends
from fastapi.responses import JSONResponse
from core.security.security import require_auth
from db.mongodb import Sessions
from fastapi_versioning import version
from bson.json_util import dumps

router = APIRouter()


@router.get("/getAll/{userId}")
@version(1)
def get_all_sessions(userId: str, auth: dict = Depends(require_auth)):
    try:
        session_data = list(Sessions.find({"userId": userId}))

        if not session_data:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"error": "Sessions does not exist."},
            )

        return JSONResponse(status_code=status.HTTP_200_OK, content=session_data)

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": f"{str(error)}"},
        )
