# Ecommerce API with FastAPI

This is a simple ecommerce API built using the FastAPI framework. It provides endpoints for managing products, orders, and users.

## Features

- **Product Management**: Create, read, update products.
- **Order Management**: Create, read, update, orders.
- **Database Integration**: Uses SQLAlchemy to interact with a database (e.g., PostgreSQL).
- **Containerization**: Includes a Dockerfile for easy deployment.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- (Optional) Docker

### Installation

1. Clone the repository:

```
git clone https://github.com/elams18/ecommerce-fastapi.git
```

2. Change to the project directory:

```
cd ecommerce-fastapi
```

3. Create a virtual environment and activate it:

```
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```
5. Add dummy data to the DB(optional)

```
python -m ecommerce.scripts.create_dummy_data
```
6. Start the development server:

```
uvicorn ecommerce.main:app --reload
```

The API will be available at `http://localhost:8000`.

### Docker

1. Build the Docker-Compose image:

```
docker-compose build
```

2. Run the Docker Compose :

```
docker-compose up -d
```

The API will be available at `http://localhost:8000`.

## API Documentation

The API documentation is generated using Swagger UI and can be accessed at `http://localhost:8000/docs`.

## Contributing

Contributions are welcome! Please follow the standard GitHub workflow:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the [MIT License](LICENSE).

