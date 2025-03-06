from decimal import Decimal
from typing import Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field

from ecommerce.core.models.order import OrderStatus


class CreateOrderProducts(BaseModel):
    product_id: int
    quantity: int


class CreateOrder(BaseModel):
    order_items: List[CreateOrderProducts]


class OrderItemInput(BaseModel):
    product_id: int
    quantity: int


class OrderItemSchema(BaseModel):
    product_id: int
    order_id: Optional[int] = None
    quantity: int
    model_config = ConfigDict(from_attributes=True)


class OrderSchema(BaseModel):
    id: Optional[int] = None
    total_price: Decimal
    status: OrderStatus
    items: List[OrderItemSchema]
    model_config = ConfigDict(from_attributes=True)


class OrderResponse(BaseModel):
    id: int
    total_price: Decimal
    status: OrderStatus
    items: List[OrderItemSchema]
