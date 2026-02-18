from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import Engine

engine: Engine = create_engine ("sqlite:///./app.db", echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    with Session(bind=engine) as session:
        yield session
