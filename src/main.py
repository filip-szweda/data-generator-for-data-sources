from random import randint, uniform, choice
from datetime import date, timedelta
import csv
from itertools import chain

from faker import Faker
from faker_food import FoodProvider

OUT_PATH = "../out/"

fake = Faker()
fake.add_provider(FoodProvider)


def fake_phone_number() -> str:
    return f'{fake.msisdn()[4:]}'


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


class OrderSQL:
    def __init__(self, order_id, phone_nb):
        self.order_id = order_id
        self.creation_date = fake.date()
        self.phone_nb = phone_nb

    def __iter__(self):
        return iter([self.order_id, self.creation_date, self.phone_nb])


class OrdersItemSQL:
    def __init__(self, dish_id, order_id):
        self.dish_id = dish_id
        self.number = randint(1, 10)
        self.order_id = order_id

    def __iter__(self):
        return iter([self.dish_id, self.number, self.order_id])


class DishSQL:
    def __init__(self, dish_id, ad_id):
        self.dish_id = dish_id
        self.name = fake.dish()
        self.price = round(uniform(20, 80), 2)
        self.ad_id = ad_id

    def __iter__(self):
        return iter([self.dish_id, self.name, self.price, self.ad_id])


class AdSQL:
    def __init__(self, ad_id):
        self.ad_id = ad_id
        self.cost = round(uniform(2000, 100000), 2)
        self.start_date = fake.date_between_dates(date_start=date(2021, 1, 1), date_end=date(2021, 12, 31))
        self.end_date = fake.date_between_dates(date_start=self.start_date, date_end=date(2021, 12, 31))

    def __iter__(self):
        return iter([self.ad_id, self.cost, self.start_date, self.end_date])


class PromotionSQL:
    def __init__(self, promotion_id, dish_id):
        self.promotion_id = promotion_id
        self.worth = randint(10, 90)
        self.start_date = fake.date_between_dates(date_start=date(2021, 1, 1), date_end=date(2021, 12, 31))
        self.end_date = fake.date_between_dates(date_start=self.start_date, date_end=date(2021, 12, 31))
        self.dish_id = dish_id

    def __iter__(self):
        return iter([self.promotion_id, self.worth, self.start_date, self.end_date, self.dish_id])


class UserXML:
    def __init__(self):
        self.phone_nb = fake_phone_number()
        self.name = fake.first_name()
        self.surname = fake.last_name()

    def __iter__(self):
        return iter([self.phone_nb, self.name, self.surname])


class AdXML:
    class ClicksPerDay:
        def __init__(self, ad_id, day):
            self.ad_id = ad_id
            self.day = day
            self.clicks = randint(1000, 100000)

        def __iter__(self):
            return iter([self.ad_id, self.day, self.clicks])

    def __init__(self, ad_id, start_date, end_date):
        self.ad_id = ad_id
        self.clicks_per_days = []
        for single_day in daterange(start_date, end_date):
            self.clicks_per_days.append(self.ClicksPerDay(self.ad_id, single_day))


ORDERS_COUNT = 1000
AD_COUNT = 100
USER_COUNT = 5000

users = []
ads_sql = []
orders = []
dishes = []
ads_xml = []
orders_items = []
promotions = []

dish_id = 0
promotion_id = 0


def generate_data():
    global dish_id
    global promotion_id

    for _ in range(USER_COUNT):
        users.append(UserXML())

    for id in range(AD_COUNT):
        ads_sql.append(AdSQL(id))

    for id in range(ORDERS_COUNT):
        orders.append(OrderSQL(id, choice(users).phone_nb))

    for ad in ads_sql:
        for _ in range(randint(1, 3)):
            dishes.append(DishSQL(dish_id, ad.ad_id))
            dish_id += 1

    for ad_sql in ads_sql:
        ads_xml.append(AdXML(ad_sql.ad_id, ad_sql.start_date, ad_sql.end_date))

    for order in orders:
        for _ in range(randint(1, 5)):
            orders_items.append(OrdersItemSQL(choice(dishes).dish_id, order.order_id))

    for dish in dishes:
        for _ in range(randint(1, 3)):
            promotions.append(PromotionSQL(promotion_id, dish.dish_id))
            promotion_id += 1


def save_to_csv(data_list, csv_filepath):
    with open(OUT_PATH + csv_filepath, "w") as stream:
        writer = csv.writer(stream)
        writer.writerows(data_list)


def save_data(suffix):
    save_to_csv(ads_sql, "ads{}.csv".format(suffix))
    save_to_csv(orders, "orders{}.csv".format(suffix))
    save_to_csv(dishes, "dishes{}.csv".format(suffix))
    save_to_csv(orders_items, "orders_items{}.csv".format(suffix))
    save_to_csv(promotions, "promotions{}.csv".format(suffix))

    save_to_csv(users, "users_xml{}.csv".format(suffix))

    iters_chain = iter(())
    for ad_xml in ads_xml:
        iters_chain = chain(iters_chain, ad_xml.clicks_per_days)
    save_to_csv(iters_chain, "ads_xml{}.csv".format(suffix))


generate_data()  # for T1
save_data("_t1")
generate_data()  # for T2
save_data("_t2")
