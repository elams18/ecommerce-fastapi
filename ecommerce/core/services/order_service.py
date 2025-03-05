from ecommerce.core.models.order import Order
from ecommerce.core.repositories.product_repository import ProductRepository


class OrderService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def create_order(self, order: Order) -> Order:
        # Fetch the product from the database
        product = self.product_repository.get_product_by_id(
            order.products[0].product_id
        )

        # Calculate the total price
        order.total_price = product.price * order.products[0].quantity

        # Save the order to the database
        return order
