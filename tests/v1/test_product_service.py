from decimal import Decimal
import pytest
from unittest.mock import AsyncMock

from ecommerce.core.models.product import Product
from ecommerce.core.repositories.product_repository import ProductRepository
from ecommerce.core.services.product_service import ProductService
from ecommerce.core.schemas.product_schema import ProductCreate


@pytest.mark.asyncio
async def test_get_products():
    product_repository = AsyncMock(ProductRepository)
    product_1 = Product(
        id=1, name="Product 1", description="Description 1", price=10.0, stock=100
    )
    product_2 = Product(
        id=2, name="Product 2", description="Description 2", price=20.0, stock=50
    )
    product_repository.get_all_products.return_value = [product_1, product_2]

    product_service = ProductService(product_repository)
    products = await product_service.get_products()

    assert len(products) == 2
    assert products[0].name == "Product 1"
    assert products[0].description == "Description 1"
    assert products[0].price == 10.0
    assert products[0].stock == 100
    assert products[1].name == "Product 2"
    assert products[1].description == "Description 2"
    assert products[1].price == 20.0
    assert products[1].stock == 50

    product_repository.get_all_products.assert_called_once()


@pytest.mark.asyncio
async def test_create_product():
    product_repository = AsyncMock(ProductRepository)
    product_create = ProductCreate(
        name="New Product",
        description="Description of the new product",
        price=Decimal(15.0),
        stock=50,
    )
    created_product = Product(
        id=1,
        name="New Product",
        description="Description of the new product",
        price=15.0,
        stock=50,
    )
    product_repository.create_product.return_value = created_product

    product_service = ProductService(product_repository)
    product = await product_service.create_product(product_create)

    assert product.id == 1
    assert product.name == "New Product"
    assert product.description == "Description of the new product"
    assert product.price == 15.0
    assert product.stock == 50

    product_repository.create_product.assert_called_once_with(product_create)


@pytest.mark.asyncio
async def test_get_product_service():
    product_repository = AsyncMock(ProductRepository)
    with pytest.raises(TypeError):
        await ProductService.get_product_service(product_repository=product_repository)
