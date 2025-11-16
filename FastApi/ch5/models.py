from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String
from db import engine


class Base(DeclarativeBase):
    pass

#USer Model/User Table
class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, email={self.email})"
    
#Create table
def create_tables():
    Base.metadata.create_all(engine)

#Drop table
def drop_tables():
    Base.metadata.drop_all(engine)