from fastapi import APIRouter

from controllers.auth import login, signup

auth_routers = APIRouter()

# auth router
auth_routers.include_router(login.router)

auth_routers.include_router(signup.router)
