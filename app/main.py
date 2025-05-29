from fastapi import FastAPI, Depends
from app.auth import authenticate
from app.db import init_db

# NOTE: you can either define the route in `app.routers.py`
# OR here directly, the choice is up to you.
from app.routers import products

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    init_db()


@app.get("/health")
async def health():
    return {"status": "ok"}


# TODO: implement logic to this effect for the `router`
# NOTE: Your challenge is to make these `products.router`.
app.include_router(
    products.router, prefix="/products", dependencies=[Depends(authenticate)]
)
