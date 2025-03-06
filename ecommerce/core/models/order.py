from enum import StrEnum, auto

from sqlalchemy import Column, Enum, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from ecommerce.core.models import Base


class OrderStatus(StrEnum):
    PENDING = auto()
    COMPLETED = auto()


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    order = relationship("Order", back_populates="items")
    product = relationship("Product")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    total_price = Column(Numeric(precision=10, scale=2))
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)

    items = relationship("OrderItem", back_populates="order")
