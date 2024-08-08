from controllers.sessions import (
    create_session,
    get_session,
    update_session,
    delete_session,
    get_all_sessions,
    delete_all_session,
)
from fastapi import APIRouter


sessions_router = APIRouter()

# Session apis

sessions_router.include_router(create_session.router)

sessions_router.include_router(get_session.router)

sessions_router.include_router(get_all_sessions.router)

sessions_router.include_router(update_session.router)

sessions_router.include_router(delete_session.router)

sessions_router.include_router(delete_all_session.router)
