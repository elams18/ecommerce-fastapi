from fastapi import Depends

from ecommerce.core.repositories.product_repository import ProductRepository
from ecommerce.core.schemas.product_schema import ProductCreate


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def get_products(self):
        return await self.product_repository.get_all_products()

    async def create_product(self, product_create: ProductCreate):
        # Add a new product to the platform. Each product should have an ID, name, description, price, and stock quantity.
        return await self.product_repository.create_product(product_create)

    @classmethod
    async def get_product_service(
        cls,
        product_repository: ProductRepository = Depends(
            ProductRepository.get_product_repository
        ),
    ):
        try:
            product_service = ProductService(product_repository)
            yield product_service
        finally:
            ...
