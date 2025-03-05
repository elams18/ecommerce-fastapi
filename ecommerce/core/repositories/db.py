async def get_db():
    try:
        db = []
        yield db
    finally:
        ...
