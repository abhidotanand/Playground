from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse

app = FastAPI()

fruits_db = {
    1: {"name": "Apple", "color": "Red"},
    2: {"name": "Banana", "color": "Yellow"},
    3: {"name": "Grapes", "color": "Purple"},
}

# @app.get("/fruits/{fruit_id}")
# async def get_fruit(fruit_id: int):
#     fruit = fruits_db.get(fruit_id)
#     if not fruit:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fruit not found", headers={"X-Error": "Fruit does not exist"})
#     return fruit




# Custome Exception Example
class FruitNotFoundException(Exception):
    def __init__(self, fruit_id: int):
        self.fruit_id = fruit_id

@app.exception_handler(FruitNotFoundException)
async def fruit_not_found_exception_handler(request: Request, exc: FruitNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"Fruit with ID {exc.fruit_id} not found."},
    )

@app.get("/fruits/{fruit_id}")
async def get_fruit(fruit_id: int):
    fruit = fruits_db.get(fruit_id)
    if not fruit:
        raise FruitNotFoundException(fruit_id)
    return fruit