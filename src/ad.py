import random
from datetime import date


class Ad:
    def __init__(self, fake, ad_id):
        self.ad_id = ad_id
        self.company = fake.company()
        self.cost = round(random.uniform(2000, 100000), 2)
        self.start_date = fake.date_between_dates(date_start=date(2021, 1, 1), date_end=date(2021, 12, 31))
        self.end_date = fake.date_between_dates(date_start=self.start_date, date_end=date(2021, 12, 31))

    def __iter__(self):
        return iter([self.ad_id, self.cost, self.company, self.start_date, self.end_date])
