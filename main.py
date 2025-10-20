from fastapi import FastAPI
from routers import admin, customer, restaurant


app = FastAPI()
app.include_router(admin.router, tags=["Admin"])
app.include_router(customer.router, tags=["Customer"])
app.include_router(restaurant.router, tags=["Restaurant"])


@app.get("/")
async def root():
    return "Welcome to Mini Swiggy"
