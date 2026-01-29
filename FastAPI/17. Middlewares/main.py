from fastapi import FastAPI
# from middlewares import first_middleware, second_middleware
from middelwares import users_middleware, items_middleware, first_middleware, second_middleware

app = FastAPI()

app.middleware("http")(first_middleware)
app.middleware("http")(second_middleware)

app.middleware("http")(users_middleware)
app.middleware("http")(items_middleware)

@app.get("/users")
async def read_root():
    print("Handling root endpoint")
    return {"message": "Hello, World!"}

@app.get("/items")
async def read_items():
    print("Handling items endpoint")
    return {"items": ["item1", "item2"]}