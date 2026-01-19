from fastapi import FastAPI
from typing import Annotated, Any
from pydantic import BaseModel

app = FastAPI()

class BaseUser(BaseModel):
    username: str
    email: str
    usertype: str = "regular"

class UserInDB(BaseUser):
    password: str

# @app.post("/users/")
# async def create_user(user: Annotated[UserInDB, "User data"]) -> BaseUser:
#     return user

@app.post("/users/", response_model=BaseUser, response_model_exclude_defaults=True)
async def create_user(user: Annotated[UserInDB, "User data"]) -> Any:
    return user

@app.post("/users/", response_model=BaseUser, response_model_include={"username", "email"})
async def create_user(user: Annotated[UserInDB, "User data"]) -> Any:
    return user