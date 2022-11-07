from random import randint, uniform, choice
from datetime import date, timedelta

from faker import Faker
from faker_food import FoodProvider

fake = Faker()
fake.add_provider(FoodProvider)


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


class OrderSQL:
    def __init__(self, order_id, phone_nb):
        self.order_id = order_id
        self.creation_date = fake.date()
        self.phone_nb = phone_nb


class OrdersItemSQL:
    def __init__(self, dish_id, order_id):
        self.dish_id = dish_id
        self.number = randint(1, 10)
        self.order_id = order_id


class DishSQL:
    def __init__(self, dish_id, ad_id):
        self.dish_id = dish_id
        self.name = fake.dish()
        self.price = round(uniform(20, 80), 2)
        self.ad_id = ad_id


class AdSQL:
    def __init__(self, ad_id):
        self.ad_id = ad_id
        self.cost = round(uniform(2000, 100000), 2)
        self.start_date = fake.date_between_dates(date_start=date(2021, 1, 1), date_end=date(2021, 12, 31))
        self.end_date = fake.date_between_dates(date_start=self.start_date, date_end=date(2021, 12, 31))


class PromotionSQL:
    def __init__(self, promotion_id, dish_id):
        self.promotion_id = promotion_id
        self.worth = randint(10, 90)
        self.start_date = fake.date_between_dates(date_start=date(2021, 1, 1), date_end=date(2021, 12, 31))
        self.end_date = fake.date_between_dates(date_start=self.start_date, date_end=date(2021, 12, 31))
        self.dish_id = dish_id


class UserXML:
    def __init__(self):
        self.phone_nb = fake.phone_number()
        self.name = fake.first_name()
        self.surname = fake.last_name()


class AdXML:
    class ClicksPerDay:
        def __init__(self, day):
            self.day = day
            self.clicks = randint(1000, 100000)

    def __init__(self, ad_id, start_date, end_date):
        self.ad_id = ad_id
        self.clicks_per_days = []
        for single_day in daterange(start_date, end_date):
            self.clicks_per_days.append(self.ClicksPerDay(single_day))


ORDERS_COUNT = 1000
AD_COUNT = 100
USER_COUNT = 5000

users = []
for _ in range(USER_COUNT):
    users.append(UserXML())

ads_sql = []
for id in range(AD_COUNT):
    ads_sql.append(AdSQL(id))

orders = []
for id in range(ORDERS_COUNT):
    orders.append(OrderSQL(id, choice(users).phone_nb))

dishes = []
dish_id = 0
for ad in ads_sql:
    for _ in range(randint(1, 3)):
        dishes.append(DishSQL(dish_id, ad.ad_id))
        dish_id += 1

ads_xml = []
for ad_sql in ads_sql:
    ads_xml.append(AdXML(ad_sql.ad_id, ad_sql.start_date, ad_sql.end_date))

orders_items = []
for order in orders:
    for _ in range(randint(1, 5)):
        orders_items.append(OrdersItemSQL(choice(dishes).dish_id, order.order_id))

promotions = []
promotion_id = 0
for dish in dishes:
    for _ in range(randint(1, 3)):
        promotions.append(PromotionSQL(promotion_id, dish.dish_id))
        promotion_id += 1
