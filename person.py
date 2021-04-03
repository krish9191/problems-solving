class Person:
    def __init__(self, name, age, profession, address, email, phone_number, car):
        self.name = name
        self.age = age
        self.job = profession
        self.address = address
        self.email = email
        self.mobile = phone_number
        self.f_members = 0
        self.license = True
        self.own_car = False
        self.car = car

    def valid_driver(self):
        if self.license:
            print('you can drive a car')
        else:
            print('get your license first')

    def purpose(self):
        if self.job == 'driver':
            print('you need a car ')
        else:
            print('purpose of buying:')

    def get_first_car(self):
        if self.own_car:
            self.own_car = not self.own_car

