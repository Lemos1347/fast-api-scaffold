from src.models import Users
from src.repository import UsersRepository

from backend.src.models.enums import UserRoles
from backend.src.schema.dtos.users_dto import UserCreationInputDTO


class UsersService:
    def __init__(self, users_repository: UsersRepository) -> None:
        self.users_repository = users_repository

    async def create_user(self, user_info: UserCreationInputDTO) -> Users:
        return await self.users_repository.create(
            user_name=user_info.user_name,
            user_email=user_info.user_email,
            password=user_info.password,
            role=UserRoles.ADMIN,
        )
