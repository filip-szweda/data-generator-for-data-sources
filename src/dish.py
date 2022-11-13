import random


class Dish:
    def __init__(self, fake, dish_id):
        self.dish_id = dish_id
        self.name = fake.dish() + " with " + random.choice([fake.ingredient(), fake.vegetable()]).lower()
        self.price = round(random.uniform(20, 80), 2)

    def __iter__(self):
        return iter([self.dish_id, self.name, self.price])
