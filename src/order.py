class Order:
    def __init__(self, fake, order_id, phone_nb, start_date, end_date):
        self.order_id = order_id
        self.creation_date = fake.date_between_dates(date_start=start_date, date_end=end_date)
        self.phone_nb = phone_nb

    def __iter__(self):
        return iter([self.order_id, self.creation_date, self.phone_nb])
