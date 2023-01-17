from datetime import date, timedelta
import random


class Promotion:
    def __init__(self, fake, promotion_id, dish_id, dish_ad_start_date, start_date, end_date):
        self.promotion_id = promotion_id
        self.worth = random.randint(10, 90)
        if dish_ad_start_date:
            self.start_date = fake.date_between_dates(
                date_start=(dish_ad_start_date - timedelta(days=random.randint(1, 31))), date_end=end_date)
        else:
            self.start_date = fake.date_between_dates(date_start=start_date, date_end=end_date)
        self.end_date = fake.date_between_dates(date_start=self.start_date, date_end=end_date)
        self.dish_id = dish_id

    def __iter__(self):
        return iter([self.promotion_id, self.worth, self.start_date, self.end_date, self.dish_id])
