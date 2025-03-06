from dotenv import load_dotenv

load_dotenv()

from ecommerce.core.config.db import DB_URL

__all__ = ["DB_URL"]
