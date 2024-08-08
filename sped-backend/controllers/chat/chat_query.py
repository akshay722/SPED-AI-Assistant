from fastapi import APIRouter, HTTPException, Request, status
from fastapi_versioning import version
from fastapi.responses import JSONResponse
from services.chat_service import handle_chat_query


router = APIRouter()


@router.post("/query")
@version(1)
async def chat_query(request: Request):
    try:
        data = await request.json()
        query = data.get("query")
        if not query:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"error": "Query is required"},
            )

        response = await handle_chat_query(query)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"status": "success", "response": response},
        )
    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": str(error)},
        )
