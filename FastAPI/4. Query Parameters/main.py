from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99},
    {"id": 3, "name": "Tablet", "price": 299.99},
]

# @app.get("/products")
# async def get_products(name: Annotated[str | None, Query(max_length=5)] = None
#                        , max_price: Annotated[float | None, Query(gt=0, lt=10000)] = None):
#     filtered_products = products
#     if name:
#         filtered_products = [product for product in filtered_products if name.lower() in product["name"].lower()]
#     if max_price is not None:
#         filtered_products = [product for product in filtered_products if product["price"] <= max_price]
#     return filtered_products


@app.get("/products")
async def get_products(search: Annotated[list[str] | None, Query(alias="q", title="Search terms", description="List of search terms")] = None):
    filtered_products = products
    if search:
        filtered_products = [product for product in filtered_products if any(term.lower() in product["name"].lower() for term in search)]
    return filtered_products


@app.get("/products")
async def get_products(search: Annotated[list[str] | None, Query(deprecated=True)] = None):
    filtered_products = products
    if search:
        filtered_products = [product for product in filtered_products if any(term.lower() in product["name"].lower() for term in search)]
    return filtered_products