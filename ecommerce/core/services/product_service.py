from fastapi import Depends
from ecommerce.core.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def get_products(self):
        return self.product_repository.get_all_products()

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
