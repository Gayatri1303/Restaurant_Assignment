from fastapi.routing import APIRouter
from repository.data_handler import Admin
from routers.DTO.restaurant_dto import Restaurant
from routers.DTO.customer_dto import Customer


router = APIRouter(prefix="/admin")
admin = Admin()


@router.get("/")
async def root():
    return "This is the admin root"


@router.post("/create_restaurant")
async def create_restaurant(restaurant_name: Restaurant):
    admin.add_restaurant(restaurant_name.name)
    return "Restaurant Added Successfully"


@router.post("/block_customer")
async def block_customer(customer_name: Customer):
    admin.block_customer(customer_name.name)
    return "Customer Blocked Successfully"


@router.post("/create_customer")
async def create_customer(customer_name: Customer):
    admin.add_customer(customer_name.name)
    return "Customer Created Successfully"


@router.post("/block_restaurant")
async def block_restaurant(restaurant_name: Restaurant):
    admin.block_restaurant(restaurant_name.name)
    return "Restaurant Blocked Successfully"


@router.delete("/remove_restaurant")
async def remove_restaurant(restaurant_name: Restaurant):
    admin.remove_restaurant(restaurant_name.name)
    return "Restaurant Removed Successfully"
