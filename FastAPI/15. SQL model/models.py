from sqlmodel import SQLModel, Field, Relationship

#Many to many relationship example
class UserAddressLink(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True, ondelete="CASCADE")
    address_id: int = Field(foreign_key="address.id", primary_key=True, ondelete="CASCADE")

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str

    posts: list["Post"] = Relationship(back_populates="user", cascade_delete=True)
    profile: "Profile" = Relationship(back_populates="user", cascade_delete=True)
    addresses: list["Address"] = Relationship(back_populates="users", link_model=UserAddressLink, sa_relationship_kwargs={"cascade": "all, delete"})

#one to many relationship example
class Post(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    content: str
    user_id: int = Field(foreign_key="user.id", ondelete="SET NULL", nullable=True)

    user: "User" = Relationship(back_populates="posts")

#One to one relationship example
class Profile(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    bio: str
    user_id: int = Field(foreign_key="user.id", unique=True, ondelete="CASCADE")

    user: "User" = Relationship(back_populates="profile")

class Address(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    street: str
    city: str

    users: list["User"] = Relationship(back_populates="addresses", link_model=UserAddressLink, sa_relationship_kwargs={"cascade": "all, delete"})