from fastapi import FastAPI, Cookie
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

# class ProductCookie(BaseModel):
#     session_id: str | None = None

# @app.get("/items/")
# async def read_items(product_cookie: Annotated[ProductCookie, Cookie()] = None):
#     if product_cookie:
#         return {"product_cookie": product_cookie}
#     return {"message": "No product_cookie cookie sent"}



#Forbid extra parameter in cookies

class ProductCookie(BaseModel):
    model_config = {
        "extra": "forbid"
    }
    session_id: str | None = None

@app.get("/items/")
async def read_items(product_cookie: Annotated[ProductCookie, Cookie()] = None):
    if product_cookie:
        return {"product_cookie": product_cookie}
    return {"message": "No product_cookie cookie sent"}