from decimal import Decimal
from typing import List
from uuid import UUID

from fastapi import Depends
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from ecommerce.core.models import get_db
from ecommerce.core.models.product import Product
from ecommerce.core.schemas.product_schema import ProductCreate


class ProductRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_all_products(self) -> List[ProductCreate]:
        # Fetch all products from the database
        async with self.db as session:
            result = await session.execute(select(Product))
            return [
                ProductCreate.model_validate(product)
                for product in result.scalars().all()
            ]

    async def create_product(self, product_create: ProductCreate) -> Product:
        # Create a new product in the database
        async with self.db as session:
            product = Product(**product_create.model_dump())
            session.add(product)
            await session.commit()
            await session.refresh(product)
            return product

    async def get_product_by_ids(self, product_ids: List[int]) -> List[Product]:
        select_statement = select(Product).where(Product.id.in_(product_ids))

        async with self.db as session:
            result = await session.execute(select_statement)
            return [product for product in result.scalars().all()]

    async def update_product(self, product: Product):
        query = (
            update(Product)
            .where(Product.id == product.id)
            .values(
                name=product.name,
                description=product.description,
                price=product.price,
                stock=product.stock,
            )
            .returning(Product)
        )
        async with self.db as session:
            updated_product = await session.execute(query)
            updated_product = updated_product.scalar_one_or_none()
            if updated_product:
                await session.commit()
                return ProductCreate.model_validate(updated_product)
            else:
                raise Exception("Failed to update product")

    @classmethod
    def get_product_repository(cls, db=Depends(get_db)) -> "ProductRepository":
        return cls(db)
