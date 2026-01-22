from db import engine
from sqlmodel import Session, SQLModel
from models import User, Post

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_user(name: str, email: str):
    with Session(engine) as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

def create_post(title: str, content: str, user_id: int):
    with Session(engine) as session:
        post = Post(title=title, content=content, user_id=user_id)
        session.add(post)
        session.commit()
        session.refresh(post)
        return post

def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()

def delete_post(post_id: int):
    with Session(engine) as session:
        post = session.get(Post, post_id)
        if post:
            session.delete(post)
            session.commit()