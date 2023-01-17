import random


class Ad:
    def __init__(self, fake, ad_id, dish_id, from_date, to_date):
        self.ad_id = ad_id
        self.company = fake.company()
        self.cost = round(random.uniform(2000, 100000), 2)
        self.start_date = fake.date_between_dates(date_start=from_date, date_end=to_date)
        self.end_date = fake.date_between_dates(date_start=self.start_date, date_end=to_date)
        self.dish_id = dish_id

    def __iter__(self):
        return iter([self.ad_id, self.cost, self.company, self.start_date, self.end_date, self.dish_id])
