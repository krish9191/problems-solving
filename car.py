class car:
    def __init__(self, brand, model, type, colour, seated):
        self.brand = brand
        self.model = model
        self.type = type
        self.colour = colour
        self.seats = seated
        self.lock = True
        self.fuel_quantity = 0
        self.speed = 0

    def drive(self, speed):
        self.speed = speed
        if speed >= 70:
            print('you cross speed limit, slow down your vehicle ')
        else:
            print('your driving is cool')

    def fuel_refill(self, quantity):
        self.fuel_quantity = quantity

    def lock(self):
        self.lock = True

    def unlock(self):
        if self.lock:
            self.lock = not self.lock

    def park(self):
        pass


c = car('Ford', 'Mustang', 'manual', 'red', 4)
c.unlock()

class person:
    import class car:
    def __init__(self,Name,age,proffession,address,email,phone_number):
        self.name=Name
        self.age=age
        self.job=proffession
        self.address=address
        self.email=email
        self.mobile=phone_number
        self.f_members=0
        self.license=True
        self.own_car=False
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
           self.own_car=not self.own_car




