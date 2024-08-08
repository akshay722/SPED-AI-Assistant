from fastapi import APIRouter

from controllers.chat import chat_query

chat_router = APIRouter()

# chat router
chat_router.include_router(chat_query.router)
