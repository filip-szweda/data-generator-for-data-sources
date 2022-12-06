from datetime import date


class Order:
    def __init__(self, fake, order_id, phone_nb):
        self.order_id = order_id
        self.creation_date = fake.date_between_dates(date_start=date(2021, 1, 1), date_end=date(2021, 12, 31))
        self.phone_nb = phone_nb

    def __iter__(self):
        return iter([self.order_id, self.creation_date, self.phone_nb])
