from fastapi import APIRouter

router = APIRouter(tags=["users"])

@router.get("/")
async def read_user():
    return {"username": "john_doe", "email": "john@example.com"}

@router.get("/me")
async def read_current_user():
    return {"username": "current_user", "email": "current@example.com"}

@router.get("/{user_id}")
async def read_user_by_id(user_id: int):
    return {"user_id": user_id, "username": f"user_{user_id}", "email": f"user_{user_id}@example.com"}