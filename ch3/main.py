from fastapi import FastAPI, HTTPException, status

app = FastAPI()

fruits_db = {
    "apple": "A sweet red fruit",
    "banana": "A long yellow fruit",
    "orange": "A round orange fruit"
}

#Using HTTPException for error handling
# @app.get("/fruits/{fruit_name}")
# async def get_fruit_description(fruit_name: str):
#     description = fruits_db.get(fruit_name)
#     if description:
#         return {"fruit": fruit_name, "description": description}
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fruit not found")

#Adding Custom Headers in Exception Responses
@app.get("/fruits_with_headers/{fruit_name}")
async def get_fruit_description_with_headers(fruit_name: str):
    description = fruits_db.get(fruit_name)
    if description:
        return {"fruit": fruit_name, "description": description}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fruit not found",
            headers={"X-Error": "FruitNotFound"}
        )