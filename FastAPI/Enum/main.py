from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# class ProductCategory(str, Enum):
#     electronics = "electronics"
#     clothing = "clothing"
#     books = "books"

# #Get products by category
# @app.get("/products/category/{category}")
# async def get_products_by_category(category: ProductCategory):
#     sample_products = {
#         "electronics": [
#             {"product_id": 1, "name": "Smartphone", "price": 699.99},
#             {"product_id": 2, "name": "Laptop", "price": 999.99},
#         ],
#         "clothing": [
#             {"product_id": 3, "name": "T-Shirt", "price": 19.99},
#             {"product_id": 4, "name": "Jeans", "price": 49.99},
#         ],
#         "books": [
#             {"product_id": 5, "name": "Fiction Book", "price": 14.99},
#             {"product_id": 6, "name": "Science Book", "price": 29.99},
#         ],
#     }
#     return sample_products[category]

# Define the Enum for product categories
class ProductCategory(str, Enum):
    electronics = "electronics"
    clothing = "clothing"
    books = "books"

@app.get("/products/category/{category}")
async def get_products_by_category(category: ProductCategory):
    if category == ProductCategory.electronics:
        return [
            {"product_id": 1, "name": "Smartphone", "price": 699.99},
            {"product_id": 2, "name": "Laptop", "price": 999.99},
        ]
    elif category.value == "clothing":
        return [
            {"product_id": 3, "name": "T-Shirt", "price": 19.99},
            {"product_id": 4, "name": "Jeans", "price": 49.99},
        ]
    elif category.value == ProductCategory.books:
        return [
            {"product_id": 5, "name": "Fiction Book", "price": 14.99},
            {"product_id": 6, "name": "Science Book", "price": 29.99},
        ]
    else:
        return ["No products found in this category."]