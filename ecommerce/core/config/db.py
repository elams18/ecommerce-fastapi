import os


def getenv_safe(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        print(f"Environment variable {key} not set!")
        raise KeyError
    return value


DB_SERVER = getenv_safe("DB_SERVER")
DB_PORT = getenv_safe("DB_PORT")

DB_NAME = getenv_safe("DB_NAME")
DB_USER = getenv_safe("DB_USER")
DB_PASSWORD = getenv_safe("DB_PASSWORD")

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
DB_SYNC_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
)
