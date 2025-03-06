from fastapi import HTTPException, status


class ProductNotInStock(HTTPException):
    def __init__(self, product_id: int, quantity: int, stock: int):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "product_id": product_id,
                "requested_quantity": quantity,
                "available_stock": stock,
            },
        )
