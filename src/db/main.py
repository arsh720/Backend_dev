# Inside src/db/main.py
from sqlmodel import SQLModel, create_engine
from src.config import Config
from src.books.models import Book

engine = create_engine(
    url=Config.DATABASE_URL,
    echo=True
)

def initdb():
    """Create our database models in the database."""
    SQLModel.metadata.create_all(engine)