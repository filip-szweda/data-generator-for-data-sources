import random

class OrdersItem:
    def __init__(self, id, dish_id, order_id):
        self.id = id
        self.dish_id = dish_id
        self.number = random.randint(1, 10)
        self.order_id = order_id

    def __iter__(self):
        return iter([self.id, self.dish_id, self.number, self.order_id])