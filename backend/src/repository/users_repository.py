from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.models import Users
from backend.src.models.enums import UserRoles


class UsersRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        return

    async def create(
        self, user_name: str, user_email: str, password: str, role: UserRoles
    ) -> Users:
        user = Users(
            user_name=user_name, user_email=user_email, password=password, role=role
        )

        self.session.add(user)

        await self.session.flush()

        return user
