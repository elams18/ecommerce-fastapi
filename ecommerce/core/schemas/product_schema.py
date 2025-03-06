from decimal import Decimal

from pydantic import BaseModel
from pydantic.config import ConfigDict


class ProductCreate(BaseModel):
    name: str
    description: str
    price: Decimal
    stock: int
    model_config = ConfigDict(from_attributes=True)
