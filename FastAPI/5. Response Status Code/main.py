from fastapi import FastAPI, status

app = FastAPI()

Products = [{"product_id": 1, "name": "Sample Product 1", "price": 19.99},
            {"product_id": 2, "name": "Sample Product 2", "price": 29.99},
            {"product_id": 3, "name": "Sample Product 3", "price": 39.99}]

@app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
async def find_product(product_id: int):
    for product in Products:
        if product["product_id"] == product_id:
            return product
    return {"message": "Product not found."}

@app.get("/products/", status_code=status.HTTP_200_OK)
async def list_products():
    return Products

@app.post("/products/", status_code=status.HTTP_201_CREATED)
async def add_product(name: str, price: float):
    new_id = max(product["product_id"] for product in Products) + 1
    new_product = {"product_id": new_id, "name": name, "price": price}
    Products.append(new_product)
    return new_product

@app.put("/products/{product_id}", status_code=status.HTTP_200_OK)
async def modify_product(product_id: int, name: str, price: float):
    for product in Products:
        if product["product_id"] == product_id:
            product["name"] = name
            product["price"] = price
            return product
    return {"message": "Product not found."}

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_product(product_id: int):
    for product in Products:
        if product["product_id"] == product_id:
            Products.remove(product)
            return {"message": f"Product with ID {product_id} has been deleted."}
    return {"message": "Product not found."}