import os
from urllib import parse
from dotenv import load_dotenv


load_dotenv(".env")

class Settings:
    DEBUG = True
    PROJECT_NAME = "FastAPI Project"
    API_V1_STR = "/api/v1"
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT = os.getenv("DATABASE_PORT", 3306)
    DATABASE_USER = os.getenv("DATABASE_USER", "user")
    DATABASE_PASSWORD = parse.quote_plus(os.getenv("DATABASE_PASSWORD", "password"))
    DATABASE_NAME = os.getenv("DATABASE_NAME", "database")
    DATABASE_DIALECT = os.getenv("DATABASE_DIALECT", "mysql")
    DATABASE_URL = f"{DATABASE_DIALECT}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
