from fastapi import APIRouter

from .user import user_router
from .item import item_router

api_router = APIRouter()
api_router.include_router(user_router, prefix="/users", tags=["user"])
api_router.include_router(item_router, prefix="/items", tags=["item"])
