from fastapi.routing import APIRouter
from repository.data_handler import Restaurant
from routers.DTO.restaurant_dto import Item
from routers.DTO.customer_dto import Customer

router = APIRouter(prefix="/restaurant/{restaurant_name}")
restaurant = Restaurant()


@router.get("/")
async def root():
    return "Restaurant Home Page"


@router.post("/add_item")
async def add_item(restaurant_name: str, item: Item):
    if restaurant_name not in restaurant.blacklist:
        restaurant.add_item(restaurant_name, item.name, item.cost)
    else:
        return "This restaurant has been blacklisted"


@router.put("/update_item")
async def update_item(restaurant_name: str, item: Item):
    if restaurant_name not in restaurant.blacklist:
        restaurant.update_item(restaurant_name, item.name, item.cost)
    else:
        return "This restaurant has been blacklisted"


@router.delete("/remove_item")
async def remove_item(restaurant_name: str, item: Item):
    if restaurant_name not in restaurant.blacklist:
        restaurant.remove_item(restaurant_name, item.name)
    else:
        return "This restaurant has been blacklisted"


@router.get("/orders")
async def get_orders(restaurant_name: str):
    if restaurant_name not in restaurant.blacklist:
        return restaurant.view_orders()
    else:
        return "This restaurant has been blacklisted"


@router.post("/accept_order")
async def accept_order(restaurant_name: str, customer: Customer):
    if (
        restaurant_name not in restaurant.blacklist
        and customer.name not in restaurant.blacklist
    ):
        restaurant.accept_order(customer.name)
    else:
        return "This restaurant has been blacklisted"


@router.post("/reject_order")
async def reject_order(restaurant_name: str, customer: Customer):
    if (
        restaurant_name not in restaurant.blacklist
        and customer.name not in restaurant.blacklist
    ):
        restaurant.reject_order(customer.name)
    else:
        return "This restaurant has been blacklisted"
