from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from db import engine


class Base(DeclarativeBase):
    pass

#USer Model/User Table
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    #One to Many relationship with Post
    posts: Mapped[list["Post"]] = relationship("Post" ,back_populates="user", cascade="all, delete")

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, email={self.email})"

#Post Model/Post Table
class Post(Base):
    __tablename__ = 'posts'
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)

    #Many to One relationship with User
    user: Mapped["User"] = relationship("User", back_populates="posts")

    def __repr__(self) -> str:
        return f"Post(id={self.id}, name={self.title})"

#Create table
def create_tables():
    Base.metadata.create_all(engine)

#Drop table
def drop_tables():
    Base.metadata.drop_all(engine)