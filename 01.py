class Car:
    price = 1000000
    house_power = 100

    def house_powers(self):
        return self.house_power


class Nissan(Car):
    price = 100000
    house_power = 125

    def house_powers(self):
        print('{} - {} {}'.format(self.__class__.__name__, self.price, self.house_power))


class Kia(Car):
    price = 10000

    def house_powers(self):
        print(self.__class__.__name__, self.price, self.house_power)


nissan_auto = Nissan()
nissan_auto.house_powers()


kia = Kia()
kia.house_powers()
