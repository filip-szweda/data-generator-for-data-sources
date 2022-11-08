from faker import Faker
import datetime
import config as c
import csv


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


def fake_phone_number(fake: Faker) -> str:
    return f'{fake.msisdn()[4:]}'


def save_to_csv(data_list, csv_filepath):
    with open(c.DATABASE_OUT + csv_filepath, "w", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerows(data_list)


def save_users_to_xml(users, filepath):
    with open(c.API_OUT + filepath, "w", encoding="utf-8") as stream:
        stream.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
                     "<users xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" "
                     "xsi:noNamespaceSchemaLocation=\"../../data_schemas/api/api_users.xsd\">\n")
        for user in users:
            for line in iter(user):
                stream.write(line)
        stream.write("</users>\n")


def save_ads_to_xml(ads, filepath):
    with open(c.API_OUT + filepath, "w", encoding="utf-8") as stream:
        stream.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
                     "<ads xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" "
                     "xsi:noNamespaceSchemaLocation=\"../../data_schemas/api/api_ads.xsd\">\n")
        for ad in ads:
            for line in iter(ad):
                stream.write(line)
        stream.write("</ads>\n")

