from fastapi import Request


# MULTIPLE MIDDLEWARES EXAMPLE
async def first_middleware(request: Request, call_next):
    print(f"1st Middleware: I'm printing before the request: {request.url}")
    response = await call_next(request)
    print(f"1st Middleware: I'm printing after the request: {response.status_code}")
    return response

async def second_middleware(request: Request, call_next):
    print(f"2nd Middleware: I'm printing before the request: {request.url}")
    response = await call_next(request)
    print(f"2nd Middleware: I'm printing after the request: {response.status_code}")
    return response

# INDIVIDUAL MIDDLEWARE EXAMPLE
async def users_middleware(request: Request, call_next):
    if request.url.path.startswith("/users"):
        print(f"Users Middleware: Processing request for {request.url.path}")
    response = await call_next(request)
    return response

async def items_middleware(request: Request, call_next):
    if request.url.path.startswith("/items"):
        print(f"Items Middleware: Processing request for {request.url.path}")
    response = await call_next(request)
    return response