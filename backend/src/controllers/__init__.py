from fastapi import APIRouter

from .users import UsersRouter

EndPointsRouter = APIRouter()

EndPointsRouter.include_route(UsersRouter)
