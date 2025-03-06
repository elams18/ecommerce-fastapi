from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.pool import AsyncAdaptedQueuePool
from ecommerce.core.config.db import DB_URL

async_engine = create_async_engine(
    DB_URL,
    poolclass=AsyncAdaptedQueuePool,
    pool_size=10,
    max_overflow=20,
)

Base = declarative_base()
async_session_maker = async_sessionmaker(bind=async_engine, expire_on_commit=False)


async def get_db():
    async with async_session_maker() as db:
        yield db
