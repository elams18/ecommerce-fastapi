from fastapi import APIRouter, Depends

from ecommerce.core.schemas.order_schema import CreateOrder, OrderResponse
from ecommerce.core.services.order_service import OrderService

router = APIRouter()


@router.post("/", response_model=OrderResponse)
async def place_order(
    order: CreateOrder,
    order_service: OrderService = Depends(OrderService.get_order_service),
):
    return await order_service.create_order(order)
