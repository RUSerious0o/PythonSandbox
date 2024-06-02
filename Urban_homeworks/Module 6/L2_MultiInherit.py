class Vehicle(object):
    def __init__(self, vehicle_type=None):
        self.__vehicle_type = vehicle_type

    def get_vehicle_type(self):
        return self.__vehicle_type


class Car(object):
    def __init__(self, horse_powers, price=10 ** 6):
        self.__price = price
        self.__horse_powers = horse_powers

    def get_horse_powers(self):
        return self.__horse_powers

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class Nissan(Vehicle, Car):
    def __init__(self, horse_powers, price=10 ** 6, vehicle_type=None):
        super().__init__(vehicle_type)
        # Vehicle.__init__(self, vehicle_type)      # same result
        Car.__init__(self, horse_powers,price)

    def __str__(self):
        return 'Vehicle type: {}, horse powers: {}, price: {}'.format(
            self.get_vehicle_type(),
            self.get_horse_powers(),
            self.get_price()
        )

    def __repr__(self):
        return self.__str__()


nissans = [Nissan(172, 1.13 * 10 ** 6, 'car'),
           Nissan(133, 0.9 * 10 ** 6),
           Nissan(142)]
print(nissans)
for i in range(3):
    nissans[i].set_price(int((i + 1) * 0.7 * 10 ** 6))
print(nissans)
