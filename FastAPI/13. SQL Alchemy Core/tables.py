from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()

# user table definition
user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(length=50), nullable=False),
    Column("email", String(length=100), nullable=False, unique=True)
)


#post table definition, ONE-TO-MANY relationship with user table
post = Table(
    "post",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(length=100), nullable=False),
    Column("content", String(length=500), nullable=False),
    Column("user_id", Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False, unique=False)
)

# address table definition, ONE-TO-ONE relationship with user table
address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("street", String(length=100), nullable=False),
    Column("city", String(length=50), nullable=False),
    Column("user_id", Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False, unique=True)
)

# subscription table definition
subscription = Table(
    "subscription",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("type", String(length=50), nullable=False),
    Column("user_id", Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False, unique=False)
)

# user_subscription table definition, MANY-TO-MANY relationship between user and subscription tables
user_subscription = Table(
    "user_subscription",
    metadata,
    Column("user_id", Integer, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True),
    Column("subscription_id", Integer, ForeignKey("subscription.id", ondelete="CASCADE"), primary_key=True)
)

# function to create tables
def create_tables():
    metadata.create_all(engine)

# funcion to drop tables
def drop_tables():
    metadata.drop_all(engine)