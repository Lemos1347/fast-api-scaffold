from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKeyHeader

from src.controllers import EndPointsRouter
from src.middlewares import AuthMiddleware

app = FastAPI()

api_key_header = APIKeyHeader(name="Authorization")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.add_middleware(AuthMiddleware)

app.include_router(EndPointsRouter, dependencies=[Depends(api_key_header)])
