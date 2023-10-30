import json

with open("data/meals.json") as file:
    meals = json.load(file)

# Complete the `Order` class
# in a dedicated file,
# it must respect the
# information given in the
# docstring.

# An order can be refused if the total is more than 2000 calories or if an unknown item is ordered.

class Order:
    """
    This class represents an order.

    Arguments:
        items (list): A list of item ids.
        date (datetime): The date and time of the order.

    Class attributes:
        counter (int): A counter for the number of orders.

    Attributes:
        order_id (str): A unique identifier for the order.
        order_accepted (bool): Whether or not the order was accepted.
        order_refused_reason (str): The reason the order was refused.
        date (datetime): The date and time of the order.
        items (list): A list of item ids.

    Properties:
        calories (int): The total calories for the order.
        price (int): The total price for the order.
    """
    counter = 0

    def __init__(
        self,
        items,
        date=None
    ):
        self.order_id = f"order-{Order.counter}"
        self.items = items
        self._calories = None
        self._price = None
        self.order_accepted = False
        self.order_refused_reason = None
        self.date = date
        self.counter += 1

    @property
    def calories(self):
        total_calories = 0
        for item in self.items:
            for meal in meals:
                try:
                    if item == meal['id']:
                        total_calories += meal['calories']
                    elif item == meal['name']:
                        total_calories += meal['calories']

                    return total_calories
                except KeyError:
                    print(f"Item '{item}' not found")

    @property
    def price(self):
        total_price = 0
        for item in self.items:
            try:
                for meal in meals:
                    if item == meal['id']:
                        total_price += meal['price']
                    elif item == meal['name']:
                        total_price += meal['price']
                return total_price
            except KeyError:
                print(f"Item '{item}' not found")

    def __repr__(self):
        return f"Order(items={self.items}, date={self.date})"

    def __str__(self):
        return f"Order {self.order_id} made on {self.date} with items {self.items}."

    def accept_order(self):
        if self.calories > 2000:
            self.order_accepted = False
            self.order_refused_reason = "Too many calories."
        else:
            self.order_accepted = True
            self.order_refused_reason = None

    def print_order(self):
        print(
            f"Order {self.order_id} made on {self.date} with items {self.items}.")
        print(f"Total calories: {self.calories}")
        print(f"Total price: {self.price}")
        if self.order_accepted:
            print("Order accepted.")
        else:
            print(f"Order refused: {self.order_refused_reason}")
