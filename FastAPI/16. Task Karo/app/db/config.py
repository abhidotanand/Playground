import os
from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated
from fastapi import Depends

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'taskkaro.db')}"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]