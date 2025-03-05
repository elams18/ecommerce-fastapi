from fastapi import APIRouter, Depends
from ecommerce.core.models.order import Order
from ecommerce.core.schemas.order_schema import OrderSchema
from ecommerce.core.services.order_service import OrderService
from ecommerce.core.repositories.product_repository import ProductRepository

router = APIRouter()


@router.post("/", response_model=OrderSchema)
def create_order(order: OrderSchema, order_service: OrderService = Depends()):
    # Create a new order
    new_order = Order(**order.dict())
    return order_service.create_order(new_order)
