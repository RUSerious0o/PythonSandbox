from Figure import Figure
from math import sqrt

class Triangle(Figure):
    _required_sides_count = 3
    __SQUARE_ROUND_PRECISION = 2

    def __calc_height(self):
        self.__height = 2 * self.get_square() / min(self.get_sides())

    def __init__(self, color_RGB, *sides, filled=False):
        super().__init__(color_RGB, 0, filled)
        self.__height = 0

        self.set_sides(*sides)

    def __str__(self):
        return super().__str__() + ', height: {}'.format(round(self.__height, 1))

    def get_square(self):
        sides = self.get_sides()
        if len(sides) == 3:
            p = self.__len__() / 2
            return round(sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])), self.__SQUARE_ROUND_PRECISION)
        return 0

    def set_sides(self, *sides):
        if len(sides) == 3:
            for i in range(3):
                if sides[i] > sides[(i + 1) % 3] + sides[(i + 2) % 3]:
                    return False
        else:
            return False

        if super().set_sides(*sides):
            self.__calc_height()

    def get_height(self):
        return self.__height



if __name__ == '__main__':
    figures = [
        Triangle([10, 10, 10], 5, 6, 7),
        Triangle([10, 10, 10], 5, -6, 5),
        Triangle([10, 10, 10], 50, 6, 5),
        Triangle([10, 10, 10], 4, 6, 5, 7)
    ]
    print(*figures, sep='\n')

    figures[1].set_sides(3, 4, 6)
    print('\n', *figures, sep='\n')
