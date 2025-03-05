from decimal import Decimal
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    price: Decimal
    stock: int
