from fastapi import FastAPI
from ecommerce.v1.routes import product

app = FastAPI()

app.include_router(product.route, prefix="/products")
