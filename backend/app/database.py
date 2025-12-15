from sqlmodel import SQLModel, create_engine, Session
from typing import Generator

# Use SQLite for local development, easy to switch to Postgres via env var later
DATABASE_URL = "sqlite:///./database.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname" 

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
