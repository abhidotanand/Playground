from fastapi import FastAPI
from app.user.router import router as user_router
from app.product.router import router as product_router

app = FastAPI()

# Importing routers from user and product modules
# app.include_router(user_router, tags=["users"])
# app.include_router(product_router, tags=["products"])
app.include_router(user_router, prefix="/users")
app.include_router(product_router)

@app.get("/", tags=["root"])
async def root():
    return {"message": "Welcome to the FastAPI application with modular routers!"}