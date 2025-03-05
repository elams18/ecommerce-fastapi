from typing import List
from fastapi import APIRouter, Depends

from ecommerce.core.models.product import Product
from ecommerce.core.services.product_service import ProductService

route = APIRouter()


@route.get("/", response_model=List[Product])
async def get_products(
    product_service: ProductService = Depends(ProductService.get_product_service),
):
    return await product_service.get_products()
