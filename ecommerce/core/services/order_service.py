from decimal import Decimal
from typing import List

from fastapi import Depends

from ecommerce.core.exceptions import ProductNotInStock
from ecommerce.core.models.order import Order, OrderItem, OrderStatus
from ecommerce.core.models.product import Product
from ecommerce.core.repositories.order_repository import OrderRepository
from ecommerce.core.repositories.product_repository import ProductRepository
from ecommerce.core.schemas.order_schema import (
    CreateOrder,
    OrderItemSchema,
    OrderResponse,
    OrderSchema,
)


class OrderService:
    def __init__(
        self, order_repository: OrderRepository, product_repository: ProductRepository
    ):
        self.order_repository = order_repository
        self.product_repository = product_repository

    async def create_order(self, create_order: CreateOrder) -> OrderResponse:
        product_ids = [item.product_id for item in create_order.order_items]
        products = await self.product_repository.get_product_by_ids(product_ids)
        await self.check_in_stock(create_order, products)

        for i, product in enumerate(products):
            product.stock -= create_order.order_items[i].quantity
            await self.product_repository.update_product(product)

        order_items = [
            OrderItemSchema(
                product_id=item.product_id,
                quantity=item.quantity,
            )
            for item in create_order.order_items
        ]
        total_price = sum([product.price for product in products], 0)
        order = OrderSchema(
            total_price=total_price, status=OrderStatus.PENDING, items=order_items
        )
        order = await self.order_repository.create_order(order)
        return order

    async def check_in_stock(self, create_order: CreateOrder, products: List[Product]):
        for product, order_item in zip(products, create_order.order_items):
            if product.stock < order_item.quantity:
                raise ProductNotInStock(product.id, order_item.quantity, product.stock)

    @classmethod
    def get_order_service(
        cls,
        order_repository: OrderRepository = Depends(
            OrderRepository.get_order_repository
        ),
        product_repository: ProductRepository = Depends(
            ProductRepository.get_product_repository
        ),
    ):
        return cls(order_repository, product_repository)
