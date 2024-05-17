from fastapi import APIRouter

from .controller import router

UsersRouter = APIRouter()

UsersRouter.include_router(router, prefix="/users", tags=["Users"])
