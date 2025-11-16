from models import User, Post
from db import SessionLocal

#Insert a new user
def create_user(name: str, email: str) -> User:
    with SessionLocal() as session:
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

#Insert a new post
def create_post(user_id: int, title: str, content: str) -> Post:
    with SessionLocal() as session:
        new_post = Post(user_id=user_id, title=title, content=content)
        session.add(new_post)
        session.commit()
        session.refresh(new_post)
        return new_post

#Get user by ID
def get_user(user_id: int) -> User:
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            return user
    return None

#Get a post by ID
def get_post(post_id: int) -> Post:
    with SessionLocal() as session:
        post = session.get(Post, post_id)
        if post:
            return post
        return None

#Get a post by user ID
def get_posts_by_user(user_id: int) -> list[Post]:
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            return user.posts
        return []

#Delete a user by ID
def delete_user(user_id: int) -> bool:
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

#Delete a post by ID
def delete_post(post_id: int) -> bool:
    with SessionLocal() as session:
        post = session.get(Post, post_id)
        if post:
            session.delete(post)
            session.commit()
            return True
        return False

#Update user email
def update_user_email(user_id: int, new_email: str) -> User:
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            user.email = new_email
            session.commit()
            session.refresh(user)
            return user
        return None

#Delete all posts by user ID
def delete_posts_by_user(user_id: int) -> int:
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            count = len(user.posts)
            for post in user.posts:
                session.delete(post)
            session.commit()
            return count
        return 0