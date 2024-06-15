class Vehicle:
    __COLOR_VARIANTS = ['white', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color if color in self.__COLOR_VARIANTS else self.__COLOR_VARIANTS[0]

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()} {self.get_horsepower()} {self.get_color()} Владелец {self.owner}')

    def set_color(self, new_color):
        if str.lower(new_color) in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Невозможно покрасить в цвет: {new_color}')


class Sedan(Vehicle):
    __PASSANGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        Vehicle.__init__(self, owner, model, color, engine_power)


if __name__ == '__main__':
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()