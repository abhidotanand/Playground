from db import engine
from tables import user, profile, posts
from sqlalchemy import insert, select, update, delete

#Insert or create User
def create_user(name: str, email: str, age: int):
    stmt = insert(user).values(name=name, email=email, age=age)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()

#Insert or create Post
def create_post(title: str, content: str, user_id: int):
    stmt = insert(posts).values(title=title, content=content, user_id=user_id)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()
    
#Delete User by ID
def delete_user(user_id: int):
    stmt = delete(user).where(user.c.id == user_id)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()

#Delete Post by ID
def delete_post(post_id: int):
    stmt = delete(posts).where(posts.c.id == post_id)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()

#Get a User by ID
def get_user(user_id: int):
    stmt = select(user).where(user.c.id == user_id)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        return result.fetchone()

#Get post by user ID
def get_posts_by_user(user_id: int):
    stmt = select(posts).where(posts.c.user_id == user_id)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        return result.fetchall()