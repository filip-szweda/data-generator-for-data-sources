from utils import fake_phone_number


class UserXML:
    def __init__(self, fake):
        self.phone_nb = fake_phone_number(fake)
        self.name = fake.first_name()
        self.surname = fake.last_name()

    def get_xml_row(self):
        return "\t<user>\n" \
               "\t\t<firstName>{}</firstName>\n" \
               "\t\t<lastName>{}</lastName>\n" \
               "\t\t<phoneNumber>{}</phoneNumber>\n" \
               "\t</user>\n".format(self.name, self.surname, self.phone_nb)

    def __iter__(self):
        return iter([self.get_xml_row()])
