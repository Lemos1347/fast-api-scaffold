from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    def __repr__(self) -> str:
        attributes = [
            f"{key}={getattr(self, key)!r}"
            for key in self.__dict__.keys()
            if not key.startswith("_")
        ]
        return f"<{self.__class__.__name__}({', '.join(attributes)})"
