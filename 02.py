class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self):
        return 150


class Nissan(Car, Vehicle):
    price = 2000000

    def __init__(self):
        super().__init__()
        self.vehicle_type = "nissan"

    def horse_powers(self):
        return 250


nissan = Nissan()
print(nissan.horse_powers())
print(nissan.price)
print(nissan.vehicle_type)
