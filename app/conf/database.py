from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.conf import settings


engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define a context manager for the session
class SessionManager:
    def __enter__(self):
        self.session = SessionLocal()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
