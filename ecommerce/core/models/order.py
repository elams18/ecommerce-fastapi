from decimal import Decimal
from enum import StrEnum, auto
from typing import List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class OrderStatus(StrEnum):
    PENDING = auto()
    COMPLETED = auto()


class OrderItem(BaseModel):
    product_id: UUID
    quantity: int


class Order(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    products: List[OrderItem] = []
    total_price: Decimal
    status: OrderStatus = Field(default=OrderStatus.PENDING)
