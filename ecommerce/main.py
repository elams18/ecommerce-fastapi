import logging

from fastapi import FastAPI

from ecommerce.core.config.db import DB_URL
from ecommerce.core.models import Base, async_engine
from ecommerce.v1.routes import order, product

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()  # Log to the console
    ],
)


async def create_all():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def startup_event():
    await create_all()


app.include_router(product.router, prefix="/products")
app.include_router(order.router, prefix="/order")
