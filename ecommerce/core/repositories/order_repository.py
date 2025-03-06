from decimal import Decimal
from typing import List
from uuid import UUID

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from ecommerce.core.models import get_db
from ecommerce.core.models.order import Order, OrderItem
from ecommerce.core.schemas.order_schema import (
    CreateOrder,
    OrderItemSchema,
    OrderResponse,
    OrderSchema,
)


class OrderRepository:
    def __init__(self, db) -> None:
        self.db = db

    async def get_all_orders(self) -> List:
        # Fetch all products from the database
        statement = select(Order)
        async with self.db as session:
            result = await session.execute(statement)
            return result.scalars().all()

    async def create_order(self, order_schema: OrderSchema) -> OrderResponse:
        async with self.db as session:
            order = Order(
                total_price=order_schema.total_price, status=order_schema.status
            )
            session.add(order)
            await session.commit()
            # Create the OrderItem entities
            order_items = [
                OrderItem(
                    order_id=order.id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                )
                for item in order_schema.items
            ]
            session.add_all(order_items)
            await session.commit()
            # Fetch the OrderItem entities for the created Order
            order_items = await session.execute(
                select(OrderItem).where(OrderItem.order_id == order.id)
            )
            order_items = order_items.scalars().all()

            return OrderResponse(
                id=order.id,
                total_price=order.total_price,
                status=order.status,
                items=[
                    OrderItemSchema(
                        order_id=order.id,
                        product_id=item.product_id,
                        quantity=item.quantity,
                    )
                    for item in order_items
                ],
            )

    @classmethod
    def get_order_repository(cls, db=Depends(get_db)) -> "OrderRepository":
        return cls(db)
