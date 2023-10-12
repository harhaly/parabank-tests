from faker import Faker

fake = Faker('en_US')


class User:

    def __init__(self):
        self.fake = Faker()
        self.result = {}
        self.reset()

    def get_first_name(self, first_name=fake.first_name()):
        self.result['First_name'] = first_name
        return self

    def get_last_name(self, last_name=fake.last_name()):
        self.result['Last_name'] = last_name
        return self

    def get_address(self, address=fake.street_address()):
        self.result['Address'] = address
        return self

    def get_city(self, city=fake.city()):
        self.result['City'] = city
        return self

    def get_state(self, state=fake.state()):
        self.result['State'] = state
        return self

    def get_zip_code(self, zip_code=fake.zipcode()):
        self.result['Zip code'] = zip_code
        return self

    def get_phone(self, phone=fake.phone_number()):
        self.result['Phone'] = phone[:20]
        return self

    def get_ssn(self, ssn=fake.ssn()):
        self.result['SSN'] = ssn
        return self

    def get_username(self, username=fake.user_name()):
        self.result['Username'] = username
        return self

    def get_password_confirm(self, password=fake.password(length=8)):
        self.result['Password'] = password
        self.result['Confirm'] = password
        return self

    # def get_confirm(self, confirm=log_pass):
    #     self.result['Confirm'] = confirm
    #     return self

    def reset(self):
        self.get_first_name()
        self.get_last_name()
        self.get_address()
        self.get_city()
        self.get_state()
        self.get_zip_code()
        self.get_phone()
        self.get_ssn()
        self.get_username()
        self.get_password_confirm()
        # self.get_confirm()
        return self

    def build(self):
        return self.result
