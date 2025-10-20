from logs.custom_logger import CustomLog

custom_logger = CustomLog()


class Admin:
    restaurant_list = []
    menu = []
    orders = []
    blacklist = []
    customer = []

    def add_restaurant(self, restaurant_name):
        Admin.restaurant_list.append(restaurant_name)

    def add_customer(self, customer_name):
        Admin.customer.append(customer_name)

    def remove_restaurant(self, restaurant_name):
        Admin.restaurant_list.remove(restaurant_name)

    def block_customer(self, customer_name):
        Admin.blacklist.append(customer_name)

    def block_restaurant(self, restaurant_name):
        Admin.blacklist.append(restaurant_name)


class Restaurant(Admin):

    def add_item(self, restaurant_name, item_name, cost):
        try:
            if not (any(item["name"] == restaurant_name for item in Admin.menu)):
                item_dict = {}
                item_dict["name"] = restaurant_name
                item_dict["menu"] = {}
                item_dict["menu"][item_name] = cost
                Admin.menu.append(item_dict)
            else:
                for restaurant in Admin.menu:
                    if restaurant["name"] == restaurant_name:
                        restaurant["menu"][item_name] = cost
        except KeyError:
            custom_logger.put_error(
                "%s: The Key being referred does not exist", __name__
            )

    def update_item(self, restaurant_name, item_name, new_value):
        try:
            for restaurant in Admin.menu:
                if restaurant["name"] == restaurant_name:
                    restaurant["menu"][item_name] = new_value
                    # key error
            else:
                custom_logger.put_error("%s: The restaurant does not exist", __name__)

        except KeyError:
            custom_logger.put_error(
                "%s: The Key being referred does not exist", __name__
            )
        except TypeError:
            custom_logger.put_error("%s: Enter name of type str not int", __name__)

    def remove_item(self, restaurant_name, item_name):
        try:
            for restaurant in Admin.menu:
                if restaurant["name"] == restaurant_name:
                    restaurant["menu"].pop(item_name)
        except KeyError:
            custom_logger.put_error(
                "%s: The Key being referred does not exist", __name__
            )

    def view_orders(self):
        return Admin.orders

    def accept_order(self, customer_name):
        order = None
        for order in Admin.orders:
            if order["name"] == customer_name:
                order["status"] = "Accepted"
                return "Order Status Changed Successfully"
        return "Name does not Exist"

    def reject_order(self, customer_name):
        order = None
        for order in Admin.orders:
            if order["name"] == customer_name:
                order["status"] = "Rejected"
                return "Order Status Changed Successfully"
        return "Name does not Exist"


class Customer(Admin):

    def view_restaurant(self):
        return Admin.restaurant_list

    def place_order(self, customer_name, restaurant_name, list_of_items):
        try:
            restaurant = None
            for rest in Admin.menu:
                if rest["name"] == restaurant_name:
                    restaurant = rest

            if restaurant:
                if not any(order["name"] == customer_name for order in Admin.orders):
                    if all(item in restaurant["menu"] for item in list_of_items):
                        order_dict = {}
                        order_dict["name"] = customer_name
                        order_dict["status"] = "Pending"
                        order_dict["order"] = list_of_items
                        Admin.orders.append(order_dict)
                    else:
                        custom_logger.put_error("%s: The item does not exist")
                else:
                    for order in Admin.orders:
                        if order["name"] == customer_name:
                            order["order"].extend(list_of_items)
            else:
                custom_logger.put_error("%s: The restaurant does not exist")
        except KeyError:
            custom_logger.put_error(
                "%s: The Key being referred does not exist", __name__
            )
        except TypeError:
            custom_logger.put_error("%s: Enter name of type str not int", __name__)

    def check_status(self, customer_name):
        order = None
        for order in Admin.orders:
            if order["name"] == customer_name:
                return order["Status"]
        return "Order Not placed"
