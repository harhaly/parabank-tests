from faker import Faker

fake = Faker('en_US')


class User:

    def __init__(self):
        self.fake = Faker()
        self.result = {}
        self.reset()

    def get_First_name(self, First_name=fake.first_name()):
        self.result['First_name'] = First_name
        return self

    def get_Last_name(self, Last_name=fake.last_name()):
        self.result['Last_name'] = Last_name
        return self

    def get_Address(self, Address=fake.street_address()):
        self.result['Address'] = Address
        return self

    def get_City(self, City=fake.city()):
        self.result['City'] = City
        return self

    def get_State(self, State=fake.state()):
        self.result['State'] = State
        return self

    def get_Zip_code(self, Zip_code=fake.zipcode()):
        self.result['Zip code'] = Zip_code
        return self

    def get_Phone(self, Phone=fake.phone_number()):
        self.result['Phone'] = Phone[:20]
        return self

    def get_SSN(self, SSN=fake.ssn()):
        self.result['SSN'] = SSN
        return self

    def get_Username(self, Username=fake.user_name()):
        self.result['Username'] = Username
        return self

    def get_Password_Confirm(self, Password=fake.password(length=8)):
        self.result['Password'] = Password
        self.result['Confirm'] = Password
        return self

    # def get_Confirm(self, Confirm=log_pass):
    #     self.result['Confirm'] = Confirm
    #     return self

    def reset(self):
        self.get_First_name()
        self.get_Last_name()
        self.get_Address()
        self.get_City()
        self.get_State()
        self.get_Zip_code()
        self.get_Phone()
        self.get_SSN()
        self.get_Username()
        self.get_Password_Confirm()
        # self.get_Confirm()
        return self

    def build(self):
        return self.result

# z = User().get_Password('sadasda').build()
# print(z)
# ('First_name', 'Last_name', 'Address', 'City', 'State', 'Zip code', 'Phone', 'SNN', f'{log}', f'{log}', f'{log}')
