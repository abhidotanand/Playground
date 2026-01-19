from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# Use pydantic model to validate request body

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax:
#         total_price = item.price + item.tax
#         item_dict.update({"total_price": total_price})
#     return item_dict


# Define multiple pydantic models for different parts of the request body
# class Product(BaseModel):
#     id: int
#     name: str
#     price: float
#     in_stock: bool = True

# class Seller(BaseModel):
#     id: int
#     name: str
#     rating: float | None = None

# @app.post("/products/")
# async def create_product(
#     sec_key:Annotated[str, Body()] ,
#     product: Product,
#     seller: Seller | None = None
#     ):
#     product_dict = product.model_dump()
#     seller_dict = seller.model_dump() if seller else None
#     return {"product": product_dict, "seller": seller_dict, "sec_key": sec_key}



#Embed

# class Product(BaseModel):
#     id: int
#     name: str
#     price: float
#     in_stock: bool = True

# @app.post("/products/")
# async def create_product(
#     product: Annotated[Product, Body(embed=True)]
#     ):
#     product_dict = product.model_dump()
#     return {"product": product_dict}

#Output with embed
# {
#   "product": {
#     "id": 0,
#     "name": "string",
#     "price": 0,
#     "in_stock": true
#   }
# }


# @app.post("/products/")
# async def create_product(
#     product: Annotated[Product, Body(embed=False)]
#     ):
#     product_dict = product.model_dump()
#     return {"product": product_dict}

#Output without embed
# {
#   "id": 0,
#   "name": "string",
#   "price": 0,
#   "in_stock": true
# }


# Pydantic fields
# class Item(BaseModel):
#     name: str = Field(title="Name of the item", max_length=50)
#     description: str | None = Field(
#         default=None,
#         title="Description of the item",
#         max_length=300,
#     )
#     price: float = Field(default=0, gt=0, description="Price must be greater than zero")
#     tax: float | None = Field(default=0, gt=0, description="Tax must be greater than zero")

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax:
#         total_price = item.price + item.tax
#         item_dict.update({"total_price": total_price})
#     return item_dict



#Pydantic model nesting
# class CategoryBase(BaseModel):
#     name: str
#     description: str | None = None

# class ProductBase(BaseModel):
#     name: str
#     price: float
#     category: CategoryBase | None = Field(default=None)

# @app.post("/items/")
# async def create_item(item: ProductBase):
#     item_dict = item.model_dump()
#     return item_dict


#Pydantic model nesting
# class CategoryBase(BaseModel):
#     name: str = Field(title="Category Name", max_length=50, examples=["Electronics", "Clothing", "Books"])
#     description: str | None = None

# class ProductBase(BaseModel):
#     name: str
#     price: float
#     category: list[CategoryBase] | None = Field(default=None)

# @app.post("/items/")
# async def create_item(item: ProductBase):
#     item_dict = item.model_dump()
#     return item_dict



#Example usage of Pydantic models
class ProductBase(BaseModel):
    name: str
    price: float
    tags: list[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Smartphone",
                    "price": 699.99,
                    "tags": ["electronics", "mobile", "gadget"]
                },
                {
                    "name": "Laptop",
                    "price": 1299.99,
                    "tags": ["electronics", "computer", "work"]
                }
            ]
        }
    }


@app.post("/items/")
async def create_item(item: ProductBase):
    item_dict = item.model_dump()
    return item_dict