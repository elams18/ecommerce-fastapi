from sqlalchemy import Column, Integer, Numeric, String

from ecommerce.core.models import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    price = Column(Numeric(precision=10, scale=2))
    stock = Column(Integer)

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"
