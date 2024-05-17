from pydantic import BaseModel

from backend.src.models.enums import UserRoles


class UserOutputDTO(BaseModel):
    user_id: str
    user_name: str
    user_email: str
    role: UserRoles


class UserCreationInputDTO(BaseModel):
    user_name: str
    user_email: str
    password: str
