from fastapi import FastAPI, Query, status, Path, Body, Cookie
from enum import Enum
from typing import Annotated, Optional
from pydantic import AfterValidator, BaseModel, Field

app = FastAPI()


#<===============HTTP PROTOCOLS==================>
# @app.get("/")
# def home():
#     return {"message": "Hello, World!"}

# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     return {"item_id": item_id}

# @app.post("/items/")
# def create_item(name: dict):
#     return {"name": name, "message": "Item created successfully!"}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, name: dict):
#     return {"item_id": item_id, "name": name, "message": "Item updated successfully!"}

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     return {"item_id": item_id, "message": "Item deleted successfully!"}

#<===============ENUM==================>
# class ProductName(str, Enum):
#     book = "book"
#     pen = "pen"
#     notebook = "notebook"

# @app.get("/products/{product_name}")
# def get_product(product_name: ProductName):
#     return {"product_name": product_name, "message": f"You selected the product: {product_name}"}

#<===============PATH PARAMETER==================>
# @app.get("/paths/{full_path:path}")
# def read_full_path(full_path: str):
#     return {"full_path": full_path}

#<===============CRUD OPERATIONS==================>
# PRODUCTS = {
#     1: {"name": "Laptop", "price": 1000},
#     2: {"name": "Smartphone", "price": 500},
#     3: {"name": "Tablet", "price": 300},
# }

# @app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
# def read_product(product_id: int):
#     product = PRODUCTS.get(product_id)
#     if product:
#         return {"product_id": product_id, "product": product}
#     return {"message": "Product not found"}

# @app.post("/products/", status_code=status.HTTP_201_CREATED)
# def create_product(product_id: int, name: str, price: float):
#     if product_id in PRODUCTS:
#         return {"message": "Product ID already exists"}
#     PRODUCTS[product_id] = {"name": name, "price": price}
#     return {"message": "Product created successfully", "product": PRODUCTS[product_id]}

# @app.put("/products/{product_id}", status_code=status.HTTP_200_OK)
# def update_product(product_id: int, name: str = None, price: float = None):
#     product = PRODUCTS.get(product_id)
#     if not product:
#         return {"message": "Product not found"}
#     if name:
#         product["name"] = name
#     if price:
#         product["price"] = price
#     return {"message": "Product updated successfully", "product": product}

# @app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_product(product_id: int):
#     if product_id in PRODUCTS:
#         del PRODUCTS[product_id]
#         return {"message": "Product deleted successfully"}
#     return {"message": "Product not found"}

#<===============USING ANNOTATED==================>
# @app.get("/item/{item_id}")
# def read_item(item_id: Annotated[int, Path(gt=0, lt=1000)]):
#     return {"item_id": item_id, "message": "Item retrieved successfully"}

# @app.get("/item/")
# def read_item(item_id: Annotated[int, Query(gt=0, lt=1000)]):
#     return {"item_id": item_id, "message": "Item retrieved successfully"}

# @app.get("/item/")
# def read_item(item_id: Annotated[list[int], Query(max_length=3)]):
#     return {"item_id": item_id, "message": "Item retrieved successfully"}

#<===============PYDANTIC EXAMPLE==================>
# def check_valid_id(item_id: int):
#     if item_id <= 0:
#         raise ValueError("item_id must be greater than 0")
#     return item_id

# @app.get("/items/{item_id}")
# def read_item(item_id: Annotated[int, AfterValidator(check_valid_id)]):
#     return {"item_id": item_id, "message": "Item retrieved successfully"}

# @app.get("/items/")
# def read_item(item_id: Annotated[int, AfterValidator(check_valid_id)]):
#     return {"item_id": item_id, "message": "Item retrieved successfully"}

#<===============PYDANTIC BASEMODEL/FIELD EXAMPLE==================>
# class Product(BaseModel):
#     name: str
#     price: float
#     stock: Optional[int] = 0

# class Seller(BaseModel):
#     name: str = Field(
#         min_length=3,
#         max_length=50,
#         description="The name of the seller",
#         example="John's Store",
#     )
#     rating: float = Field(
#         ge=0,
#         le=5,
#         description="The rating of the seller",
#         example=4.5,
#     )

# @app.post("/products/")
# def create_product(product: Product, seller: Seller, sec_key: Annotated[str, Body()]):
#     return {
#         "product": product,
#         "seller": seller,
#         "message": "Product and seller created successfully",
#         "security key": sec_key
#     }

#<===============NESTED MODEL AND EXAMPLES EXAMPLE==================>
# class Category(BaseModel):
#     name: str = Field(
#         min_length=3,
#         max_length=50,
#         examples=["Electronics", "Books", "Clothing"]
#     )
#     description: str = Field(
#         max_length=300,
#         examples=["Category for electronic items", "Category for books", "Category for clothing items"]
#     )

# class Product(BaseModel):
#     name: str = Field(
#         min_length=3,
#         max_length=100,
#         description="The name of the product",
#         examples=["Smartphone", "Laptop", "Headphones"]
#     )
#     price: float = Field(
#         gt=0,
#         description="The price of the product",
#         examples=[199.99, 499.99, 29.99]
#     )
#     stock: Optional[int] = Field(
#         default=0,
#         ge=0,
#         description="The available stock of the product",
#         examples=[10, 50, 100]
#     )
#     category: list[Category] = Field(
#         description="List of categories the product belongs to",
#         default=None,
#         examples=[
#             {"name": "Electronics", "description": "Category for electronic items"},
#             {"name": "Gadgets", "description": "Category for gadgets and devices"}
#         ]   
#     )

# @app.post("/products/")
# def create_product(product: Product):
#     return {
#         "product": product,
#         "message": "Product created successfully with categories"
#     }

#<===============COOKIES EXAMPLE==================>
# @app.post("/products/recommendations/")
# def create_product(session_id: Annotated[Optional[str], Cookie()] = None):
#     if session_id:
#         return {
#             "session_id": session_id,
#             "message": "Recommendations based on your session"
#         }
#     else:
#         return {
#             "message": "No session ID provided. Showing generic recommendations."
#         }

# class ProductRecommendations(BaseModel):
#     session_id: Optional[str] = None
#     product_category: Optional[str] = None
#     tracking_id: Optional[str] = None

# @app.post("/products/recommendations/")
# def create_product(cookie: Annotated[ProductRecommendations, Cookie()] = None):
#     if cookie.session_id:
#         if cookie.product_category:
#             return {
#                 "session_id": cookie.session_id,
#                 "product_category": cookie.product_category,
#                 "message": "Recommendations based on your session and product category"
#             }
#     return {
#         "message": "No session ID provided. Showing generic recommendations."
#     }

