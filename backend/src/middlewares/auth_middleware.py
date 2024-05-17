import jwt
from fastapi import status
from src.configs.db_config.config import SessionLocal
from src.services import get_users_service
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    DispatchFunction,
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, dispatch: DispatchFunction | None = None) -> None:
        super().__init__(app, dispatch)
        self.exclude_paths_from_middleware = ["/docs", "/docs/", "/users", "/users/"]
        self.exclude_methods_from_middleware = ["OPTIONS"]

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if request.url.path in self.exclude_paths_from_middleware:
            return await call_next(request)

        if request.method in self.exclude_methods_from_middleware:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return Response(
                content="Authorization header is missing",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        token_type, _, token = auth_header.partition(" ")

        if token_type.lower() != "bearer" or not token:
            return Response(
                content="Invalid authorization header format",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        async with SessionLocal() as session:
            await session.begin()

            self.users_service = await get_users_service(session=session)

            try:
                jwt_decoded = jwt.decode(token, options={"verify_signature": False})
                user_email = jwt_decoded.get("sub").lower()

                user = await self.users_service.get_user_for_auth(user_email)

            except jwt.PyJWTError as e:
                return Response(content=str(e), status_code=status.HTTP_403_FORBIDDEN)

            if user is None:
                return Response(
                    content="User not in DB", status_code=status.HTTP_403_FORBIDDEN
                )

            request.state.email = user_email
            request.state.user = user

            return await call_next(request)
