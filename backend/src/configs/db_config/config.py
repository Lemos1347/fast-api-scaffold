from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

DATABASE_URI = "postgresql://user:password@hostname:port/database_name"

engine = create_async_engine(DATABASE_URI, pool_size=20, max_overflow=0)

SessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db_session() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as session:
        await session.begin()
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
