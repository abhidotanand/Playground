from fastapi import APIRouter

router = APIRouter(tags=["products"], prefix="/products")

@router.get("/")
async def read_products():
    return {"products": ["product1", "product2"]}

@router.get("/{product_id}")
async def read_product_by_id(product_id: int):
    return {"product_id": product_id, "name": f"product_{product_id}"}