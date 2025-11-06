from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Column, Table
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

    #One to One relationship with Profile
    profile: Mapped["Profile"] = relationship("Profile", back_populates="user", cascade="all, delete")

    #Many to Many relationship with Address
    addresses: Mapped[list["Address"]] = relationship("Address", back_populates="user", cascade="all, delete")

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

#Profile Model/Profile Table
class Profile(Base):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(primary_key=True)
    bio: Mapped[str] = mapped_column(String(250), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"), unique=True, nullable=False)

    #One to One relationship with User
    user: Mapped["User"] = relationship("User", back_populates="profile")
    
    def __repr__(self) -> str:
        return f"Profile(id={self.id}, bio={self.bio})"

#Address Model/Address Table
class Address(Base):
    __tablename__ = 'addresses'

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    #Many to Many relationship with User
    user: Mapped[list[User]] = relationship("User", back_populates="addresses", cascade="all, delete")

    def __repr__(self) -> str:
        return f"Address(id={self.id}, street={self.street}, city={self.city})"

#Association Table for Many to Many relationship between User and Address
user_address_association = Table(
    'user_address_association', Base.metadata,
    Column('user_id', ForeignKey('users.id', ondelete="CASCADE"), primary_key=True),
    Column('address_id', ForeignKey('addresses.id', ondelete="CASCADE"), primary_key=True)
)

#Create table
def create_tables():
    Base.metadata.create_all(engine)

#Drop table
def drop_tables():
    Base.metadata.drop_all(engine)