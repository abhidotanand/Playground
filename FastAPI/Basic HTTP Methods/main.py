from fastapi import FastAPI

app = FastAPI()

#Get a product by its ID
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return {"product_id": product_id, "name": "Sample Product", "price": 19.99}

#Get all products
@app.get("/products/")
async def get_all_products():
    return [
        {"product_id": 1, "name": "Sample Product 1", "price": 19.99},
        {"product_id": 2, "name": "Sample Product 2", "price": 29.99},
    ]

#Create a new product
@app.post("/products/")
async def create_product(name: str, price: float):
    return {"product_id": 3, "name": name, "price": price}

#Update an existing product
@app.put("/products/{product_id}")
async def update_product(product_id: int, name: str, price: float):
    return {"product_id": product_id, "name": name, "price": price}

#Partially update a product
@app.patch("/products/{product_id}")
async def partial_update_product(product_id: int, name: str = None, price: float = None):
    return {"product_id": product_id, "name": name, "price": price}

#Delete a product
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    return {"message": f"Product with ID {product_id} has been deleted."}