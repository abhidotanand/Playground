from services import create_db_and_tables, create_user, create_post, delete_user, delete_post
from models import User, Post

create_db_and_tables()

user1 = User(name="Alice", email="alice@example.com")
user2 = User(name="Bob", email="bob@example.com")

post1 = Post(title="First Post", content="This is Alice's first post.", user_id=1)
post2 = Post(title="Second Post", content="This is Bob's first post.", user_id=2)

create_user(name=user1.name, email=user1.email)
create_user(name=user2.name, email=user2.email)

create_post(title=post1.title, content=post1.content, user_id=post1.user_id)
create_post(title=post2.title, content=post2.content, user_id=post2.user_id)