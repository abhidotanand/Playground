from db import engine
from tables import user, post, address, subscription, user_subscription
from sqlalchemy import insert, select, update, delete

# Insert or Create User
def create_user(name: str, email: str):
    stmt = insert(user).values(name=name, email=email)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

def delete_user(user_id: int):
    stmt = delete(user).where(user.c.id == user_id)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

def get_user(user_id: int):
    stmt = select(user).where(user.c.id == user_id)
    with engine.connect() as conn:
        result = conn.execute(stmt).fetchone()
        return result

def update_user(user_id: int, name: str = None, email: str = None):
    stmt = update(user).where(user.c.id == user_id)
    if name:
        stmt = stmt.values(name=name)
    if email:
        stmt = stmt.values(email=email)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

def create_post(title: str, content: str, user_id: int):
    stmt = insert(post).values(title=title, content=content, user_id=user_id)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

def get_posts_by_user(user_id: int):
    stmt = select(post).where(post.c.user_id == user_id)
    with engine.connect() as conn:
        result = conn.execute(stmt).fetchall()
        return result

def delete_post(post_id: int):
    stmt = delete(post).where(post.c.id == post_id)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

def update_post(post_id: int, title: str = None, content: str = None):
    stmt = update(post).where(post.c.id == post_id)
    if title:
        stmt = stmt.values(title=title)
    if content:
        stmt = stmt.values(content=content)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
