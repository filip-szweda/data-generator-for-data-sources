from datetime import date
import random


class Promotion:
    def __init__(self, fake, promotion_id, dish_id):
        self.promotion_id = promotion_id
        self.worth = random.randint(10, 90)
        self.start_date = fake.date_between_dates(date_start=date(2021, 1, 1), date_end=date(2021, 12, 31))
        self.end_date = fake.date_between_dates(date_start=self.start_date, date_end=date(2021, 12, 31))
        self.dish_id = dish_id

    def __iter__(self):
        return iter([self.promotion_id, self.worth, self.start_date, self.end_date, self.dish_id])
