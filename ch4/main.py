from tables import create_tables
from services import create_user, create_post, delete_user, delete_post, get_user, get_posts_by_user

#Create the tables
create_tables()

#Create a sample user
# create_user(name="Alice", email="alice@wonderland.com", age=28)

#Create a sample post
# create_post(title="My First Post", content="This is the content of my first post.", user_id=1)
# create_post(title="My Second Post", content="This is the content of my second post.", user_id=1)

#Delete a user by ID
# delete_user(user_id=1)

#Delete a post by ID
# delete_post(post_id=1)

#Get a user by ID
# user = get_user(user_id=1)
# print(user)

#Get posts by user ID
posts = get_posts_by_user(user_id=1)
for post in posts:
    print(post)