from fastapi import APIRouter, Depends, HTTPException
from src.schema.dtos import UserCreationInputDTO, UserOutputDTO
from src.services import UsersService, get_users_service

router = APIRouter()


@router.post("", response_model=UserOutputDTO)
async def create_user(
    body: UserCreationInputDTO, user_service: UsersService = Depends(get_users_service)
):
    try:
        await user_service.create_user(body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
