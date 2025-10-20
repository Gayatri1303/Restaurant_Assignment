from fastapi.routing import APIRouter
from fastapi import Query
from repository.data_handler import Customer
from typing import Annotated

router = APIRouter(prefix="/customer/{customer_name}")
customer = Customer()


@router.get("/")
async def root():
    return "Customer Home Page"


@router.get("/restaurant")
async def view_restaurant_list():
    return customer.view_restaurant()


@router.post("/{restaurant_name}/place_order/")
async def place_order(
    customer_name: str, restaurant_name: str, name: Annotated[list[str], Query()]
):
    if customer_name not in customer.blacklist:
        customer.place_order(customer_name, restaurant_name, name)


@router.get("/check_status")
async def check_status(customer_name: str):
    return customer.check_status(customer_name)
