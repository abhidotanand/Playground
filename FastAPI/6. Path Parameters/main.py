from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99},
    {"id": 3, "name": "Tablet", "price": 299.99},
]

@app.get("/products/{product_id}")
async def get_products(product_id: Annotated[int, Path(gt=0, title="Product ID", description="The ID of the product to retrieve")]
                       , search: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
    filtered_products = products
    if product_id:
        filtered_products = [product for product in filtered_products if product["id"] == product_id]
    if search:
        filtered_products = [product for product in filtered_products if search.lower() in product["name"].lower()]
    return filtered_products