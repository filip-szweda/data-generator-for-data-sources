import random
from faker import Faker
from faker_food import FoodProvider

import config as c
from ad_xml import AdXML

from dish import Dish
from orders_item import OrdersItem
from promotion import Promotion
from user_xml import UserXML
from ad import Ad
from order import Order


class Generator:
    def __init__(self):
        self.fake = Faker()
        self.fake.add_provider(FoodProvider)
        self.users = []
        self.ads_sql = []
        self.orders = []
        self.dishes = []
        self.ads_xml = []
        self.orders_items = []
        self.promotions = []

        self.ad_sql_id = 0
        self.promotion_id = 0
        self.orders_item_id = 0

    def generate(self):
        for _ in range(c.USER_COUNT):
            self.users.append(UserXML(self.fake))

        for dish_id in range(c.DISH_COUNT):
            self.dishes.append(Dish(self.fake, dish_id))

        for order_id in range(c.ORDERS_COUNT):
            self.orders.append(Order(self.fake, order_id, random.choice(self.users).phone_nb))

        for dish in self.dishes:
            for _ in range(random.randint(1, 3)):
                self.ads_sql.append(Ad(self.fake, self.ad_sql_id, dish.dish_id))
                self.ad_sql_id += 1

        for ad_sql in self.ads_sql:
            self.ads_xml.append(AdXML(ad_sql.ad_id, ad_sql.start_date, ad_sql.end_date))

        for order in self.orders:
            for _ in range(random.randint(1, 5)):
                self.orders_items.append(
                    OrdersItem(self.orders_item_id, random.choice(self.dishes).dish_id, order.order_id))
                self.orders_item_id += 1

        for dish in self.dishes:
            for _ in range(random.randint(1, 3)):
                dish_ads = [ad for ad in self.ads_sql if ad.dish_id == dish.dish_id]
                dish_ad_start_date = random.choice(dish_ads).start_date if dish_ads else None
                self.promotions.append(Promotion(self.fake, self.promotion_id, dish.dish_id, dish_ad_start_date))
                self.promotion_id += 1
