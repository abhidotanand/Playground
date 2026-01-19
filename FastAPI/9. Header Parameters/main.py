from fastapi import FastAPI, Header
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class ProductHeaders(BaseModel):
    # model_config = {
    #     "extra": "forbid"
    # }
    user_agent: str | None = None
    test_header: str | None = None

@app.get("/items/")
async def read_items(product_headers: Annotated[ProductHeaders, Header()] = None):
    if product_headers:
        return {"product_headers": product_headers}
    return {"message": "No product_headers header sent"}

# Output:
# $ curl http://localhost:8000/items/ -H "test-header: testing"
# {"product_headers":{"user_agent":"curl/8.5.0","test_header":"testing"}}(venv) abhi@devbox:~/Desktop/Repos$