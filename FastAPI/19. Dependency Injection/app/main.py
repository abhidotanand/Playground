from fastapi import FastAPI, Depends, Header, HTTPException
from typing import Annotated

app = FastAPI()

async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons

CommonDep = Annotated[dict, Depends(common_parameters)]

@app.get("/users/")
async def read_users(commons: CommonDep):
    return commons

# We can create hirerachal dependencies as well
async def query_extractor(q: str = None):
    return q

async def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: str = None
):
    if not q:
        return last_query
    return q

@app.get("/search/")
async def search(query_or_default: Annotated[str, Depends(query_or_cookie_extractor)]):
    return {"q": query_or_default}


# To use classes as dependencies
class CommonQueryParams:
    def __init__(self, q: str = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

# @app.get("/products/")
# async def read_products(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
#     return {"q": commons.q, "skip": commons.skip, "limit": commons.limit}

@app.get("/products/")
async def read_products(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    return {"q": commons.q, "skip": commons.skip, "limit": commons.limit}


# Dependencies in route decorators
async def verify_token(x_token: Annotated[str | None, Header()] = None):
    if x_token != "supersecrettoken":
        raise HTTPException(status_code=400, detail="X-Token header invalid.")

@app.get("/headers/", dependencies=[Depends(verify_token)])
async def read_headers():
    return {"message": "Headers are valid!"}