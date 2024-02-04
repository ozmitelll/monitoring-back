from fastapi.routing import APIRouter

from api.v1 import (
    user
)
api_router = APIRouter()
api_router.include_router(user.auth, prefix="/auth", tags=["Authentication"])
api_router.include_router(user.router, prefix="/user", tags=["User"])