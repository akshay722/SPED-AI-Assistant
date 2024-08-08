from fastapi import APIRouter

from controllers.scrape import scrape_query

chat_router = APIRouter()

# scrape router
chat_router.include_router(scrape_query.router)