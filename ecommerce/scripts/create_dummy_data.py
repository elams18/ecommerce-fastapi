import random
import typer
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from ecommerce.core.config.db import DB_URL
from ecommerce.core.models.order import Order, OrderItem, OrderStatus
from ecommerce.core.models.product import Product

app = typer.Typer()

# Initialize the database connection
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)


@app.command()
def seed_db(num_products: int = 10, num_orders: int = 5):
    """
    Seed the database with dummy data.
    """
    with Session() as session:
        # Create dummy products
        for _ in range(num_products):
            product = Product(
                name=f"Product {session.query(Product).count() + 1}",
                description="This is a sample product.",
                price=round(random.uniform(10.00, 100.00), 2),
                stock=random.randint(1, 100),
            )
            session.add(product)

        # Create dummy orders
        for _ in range(num_orders):
            order = Order(
                total_price=random.uniform(50.00, 500.00),
                status=random.choice(list(OrderStatus)),
            )
            session.add(order)

            # Add order items
            for _ in range(random.randint(1, 5)):
                product = session.query(Product).order_by(func.random()).first()
                order_item = OrderItem(
                    order_id=order.id,
                    product_id=product.id,
                    quantity=random.randint(1, 5),
                )
                session.add(order_item)

        session.commit()


if __name__ == "__main__":
    app()
