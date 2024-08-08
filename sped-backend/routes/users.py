from controllers.users import get_user
from fastapi import APIRouter


users_router = APIRouter()

# User apis

users_router.include_router(get_user.router)
