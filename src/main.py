from generator import Generator
from utils import save_to_csv, save_users_to_xml, save_ads_to_xml
import config as c


def save_data(generator, suffix):
    from pathlib import Path
    Path(c.DATABASE_OUT).mkdir(parents=True, exist_ok=True)
    Path(c.API_OUT).mkdir(parents=True, exist_ok=True)
    save_to_csv(generator.ads_sql, "ads{}.csv".format(suffix))
    save_to_csv(generator.orders, "orders{}.csv".format(suffix))
    save_to_csv(generator.dishes, "dishes{}.csv".format(suffix))
    save_to_csv(generator.orders_items, "orders_items{}.csv".format(suffix))
    save_to_csv(generator.promotions, "promotions{}.csv".format(suffix))

    save_users_to_xml(generator.users, "users{}.xml".format(suffix))
    save_ads_to_xml(generator.ads_xml, "ads{}.xml".format(suffix))


def main():
    generator = Generator()

    # T1
    generator.generate()
    save_data(generator, "_t1")

    # T2
    # generator.update_dishes()
    # generator.generate()
    # save_data(generator, "_t2")


if __name__ == "__main__":
    main()

