from typing import List

from fastapi import APIRouter, Body, Depends

from ecommerce.core.schemas.product_schema import ProductCreate
from ecommerce.core.services.product_service import ProductService

router = APIRouter()


@router.get("/", response_model=List[ProductCreate])
async def get_products(
    product_service: ProductService = Depends(ProductService.get_product_service),
):
    return await product_service.get_products()


@router.post("/")
async def create_product(
    product_create: ProductCreate = Body(),
    product_service: ProductService = Depends(ProductService.get_product_service),
):
    return await product_service.create_product(product_create)
