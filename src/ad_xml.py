import random
from utils import daterange


class AdXML:
    class ClicksPerDay:
        def __init__(self, day):
            self.day = day
            self.clicks = random.randint(1000, 100000)

        def get_xml_row(self):
            return "\t\t\t<day date=\"{}\">{}</day>\n".format(self.day, self.clicks)

    def get_xml_row(self):
        xml = "\t<ad>\n"\
              "\t\t<id>{}</id>\n" \
              "\t\t<clicksPerDay>\n".format(self.ad_id)
        for clicks_per_day in self.clicks_per_days:
            xml += f"{clicks_per_day.get_xml_row()}"
        xml += "\t\t</clicksPerDay>\n"
        xml += "\t</ad>\n"
        return xml

    def __init__(self, ad_id, start_date, end_date):
        self.ad_id = ad_id
        self.clicks_per_days = []
        for single_day in daterange(start_date, end_date):
            self.clicks_per_days.append(self.ClicksPerDay(single_day))

    def __iter__(self):
        return iter([self.get_xml_row()])
