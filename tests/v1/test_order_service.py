from unittest.mock import AsyncMock
import pytest


from ecommerce.core.repositories.order_repository import OrderRepository
from ecommerce.core.repositories.product_repository import ProductRepository
from ecommerce.core.services.order_service import OrderService
from ecommerce.core.schemas.order_schema import (
    CreateOrderProducts,
    OrderSchema,
    OrderItemSchema,
    OrderStatus,
    CreateOrder,
)
from ecommerce.core.models.product import Product
from ecommerce.core.exceptions import ProductNotInStock


@pytest.mark.asyncio
async def test_create_order_with_sufficient_stock():
    order_repository = AsyncMock(OrderRepository)
    product_repository = AsyncMock(ProductRepository)

    product_1 = Product(
        id=1, name="Product 1", description="Description 1", price=10.0, stock=100
    )
    product_2 = Product(
        id=2, name="Product 2", description="Description 2", price=20.0, stock=50
    )

    product_repository.get_product_by_ids.return_value = [product_1, product_2]
    order_repository.create_order.return_value = OrderSchema(
        id=1,
        total_price=30.0,
        status=OrderStatus.PENDING,
        items=[
            OrderItemSchema(product_id=1, quantity=2),
            OrderItemSchema(product_id=2, quantity=1),
        ],
    )

    order_service = OrderService(order_repository, product_repository)
    create_order = CreateOrder(
        order_items=[
            CreateOrderProducts(product_id=1, quantity=2),
            CreateOrderProducts(product_id=2, quantity=1),
        ]
    )

    order_response = await order_service.create_order(create_order)

    assert order_response.id == 1
    assert order_response.total_price == 30.0
    assert order_response.status == OrderStatus.PENDING
    assert len(order_response.items) == 2
    assert order_response.items[0].product_id == 1
    assert order_response.items[0].quantity == 2
    assert order_response.items[1].product_id == 2
    assert order_response.items[1].quantity == 1

    product_repository.get_product_by_ids.assert_called_once_with([1, 2])


@pytest.mark.asyncio
async def test_create_order_with_insufficient_stock():
    order_repository = AsyncMock(OrderRepository)
    product_repository = AsyncMock(ProductRepository)

    product_1 = Product(
        id=1, name="Product 1", description="Description 1", price=10.0, stock=5
    )
    product_2 = Product(
        id=2, name="Product 2", description="Description 2", price=20.0, stock=10
    )

    product_repository.get_product_by_ids.return_value = [product_1, product_2]

    order_service = OrderService(order_repository, product_repository)
    create_order = CreateOrder(
        order_items=[
            CreateOrderProducts(product_id=1, quantity=10),
            CreateOrderProducts(product_id=2, quantity=15),
        ]
    )

    with pytest.raises(ProductNotInStock) as exc:
        await order_service.create_order(create_order)

    assert exc.value.detail.get("product_id") == 1
    assert exc.value.detail.get("requested_quantity") == 10
    assert exc.value.detail.get("available_stock") == 5

    product_repository.get_product_by_ids.assert_called_once_with([1, 2])
    product_repository.update_product.assert_not_called()
    order_repository.create_order.assert_not_called()
