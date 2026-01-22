from models import create_tables, drop_tables
from models import User, Post, Profile, Address
from db import SessionLocal

create_tables()
# drop_tables()

def create_users():
    with SessionLocal() as session:
        user1 = User(name="Alice", email="alice@example.com")
        user1.posts = [
            Post(title="Alice's First Post", content="This is the content of Alice's first post."),
            Post(title="Alice's Second Post", content="This is the content of Alice's second post.")
        ]
        session.add(user1)
        session.commit()
        session.commit()
        session.refresh(user1)
        return user1

def delete_user(user_id: int):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

def delete_post(post_id: int):
    with SessionLocal() as session:
        post = session.get(Post, post_id)
        if post:
            session.delete(post)
            session.commit()
            return True
        return False

def update_post(post_id: int, new_title: str, new_content: str):
    with SessionLocal() as session:
        post = session.get(Post, post_id)
        if post:
            post.title = new_title
            post.content = new_content
            session.commit()
            session.refresh(post)
            return post
        return None

# create_users()
# delete_user(1)
# delete_post(2)
# update_post(1, "Updated Title", "Updated Content")