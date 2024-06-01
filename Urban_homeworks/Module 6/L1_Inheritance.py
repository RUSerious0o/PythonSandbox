class Car:
    __price = 10 ** 6
    __horse_powers = 100

    def get_price(self):
        return self.__price

    def get_horse_powers(self):
        return self.__horse_powers

    def set_horse_powers(self, horse_powers):
        self.__horse_powers = horse_powers

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f'{self.__class__.__name__}: price: {self.__price}, horse powers: {self.__horse_powers}'


class Nissan(Car):
    def __init__(self, price=15 * 10 ** 5, horse_powers=140):
        self.set_price(price)
        self.set_horse_powers(horse_powers)


class Kia(Car):
    def __init__(self, price=int(1.21 * 10 ** 6), horse_powers=120):
        self.set_price(price)
        self.set_horse_powers(horse_powers)


cars = [Car(), Nissan(), Kia(), Kia(2 * 10 ** 6, 200)]
print(*cars, sep='\n')
