from db import engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

user = Table(
    'user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(length=50), nullable=False),
    Column('email', String(length=100), unique=True, nullable=False),
    Column('age', Integer),
)

#1 to 1 relationship with profile
profile = Table(
    'profile', metadata,
    Column('id', Integer, primary_key=True),
    Column('bio', String(length=250)),
    Column('user_id', Integer, ForeignKey('user.id', ondelete="CASCADE"), nullable=False, unique=True),
)

#1 to many relationship with posts
posts = Table(
    'posts', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(length=200), nullable=False),
    Column('content', String, nullable=False),
    Column('user_id', Integer, ForeignKey('user.id', ondelete="CASCADE"), nullable=False),
)

def create_tables():
    metadata.create_all(engine)