from fastapi import Depends

from src.configs.db_config.config import get_db_session
from src.repository import UsersRepository

from .user_service import UsersService


async def get_users_service(session=Depends(get_db_session)) -> UsersService:
    return UsersService(UsersRepository(session))
