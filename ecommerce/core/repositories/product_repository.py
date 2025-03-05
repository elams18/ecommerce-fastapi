from decimal import Decimal
from typing import List
from uuid import UUID

from fastapi import Depends
from ecommerce.core.models.product import Product
from ecommerce.core.repositories.db import get_db


class ProductRepository:
    def __init__(self, db) -> None:
        self.db = db

    def get_all_products(self) -> List[Product]:
        # Fetch all products from the database
        return []

    def create_product(self, product: Product) -> Product:
        # Create a new product in the database
        return product

    def get_product_by_id(self, product_id: UUID) -> Product:
        product = Product(name="test", description="", price=Decimal(1.0), stock=1)
        return product

    @classmethod
    def get_product_repository(cls, db=Depends(get_db)) -> "ProductRepository":
        return cls(db)
