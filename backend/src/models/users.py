from sqlalchemy import UUID, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from .base_model import Base
from .enums import UserRoles


class Users(Base):
    __tablename__ = "users"

    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    user_name: Mapped[str] = mapped_column(Text, nullable=False)
    user_email: Mapped[str] = mapped_column(Text, nullable=False)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    role: Mapped[UserRoles] = mapped_column(Enum(UserRoles), nullable=False)
