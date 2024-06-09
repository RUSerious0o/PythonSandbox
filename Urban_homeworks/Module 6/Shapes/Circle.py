from Figure import Figure
from math import pi


class Circle(Figure):
    __ROUND_PRECISION = 1

    _required_sides_count = 1

    def __init__(self, color_RGB, sides, filled=False):
        super().__init__(color_RGB, 0, filled)
        self.__radius = 0

        self.set_sides(sides)

    def get_square(self):
        return round(pi * (self.__radius ** 2), self.__ROUND_PRECISION)


    def set_sides(self, *sides):
        if super().set_sides(*sides):
            self.__radius = sides[0] / (2 * pi)
            return  True
        else:
            return False


if __name__ == '__main__':
    figures = [
        Circle([10, -5, 10], 20, True),
        Circle([10, 10, 10], 20, True),
        Circle([10, 10, 10], 10),
        Circle([10, 10, 10], -10),
        Circle([10, 10, 10], '-10')
    ]

    print(*figures, sep='\n')
    figures[1].set_sides(10)
    print('\n', figures[1])
    figures[1].set_sides(10, 20)
    print(figures[1])
    figures[1].set_sides(2)
    print(figures[1])
