import os
from sqlalchemy import create_engine


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


class Settings:
    PROJECT_NAME: str = "MyMeal"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "mymeal")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


@singleton
class DbConnection:

    @staticmethod
    def connect():
        try:
            settings = Settings()
            engine = create_engine(settings.DATABASE_URL)
            return engine
        except Exception as ex:
            print(f'Sorry failed to connect: {ex}')
            return ex

