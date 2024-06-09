class Figure:
    __SIDES_INPUT_ERROR = 'Ошибка ввода сторон фигуры'
    __COLOR_INPUT_ERROR = 'Ошибка ввода цвета фигуры'
    __SHAPE_NOT_SET_ERROR = '0 (shape is missing or mismatch)'

    _required_sides_count = None

    def __is_valid_color(self, color_RGB=[]):
        if len(color_RGB) == 3:
            result = True
            for color in color_RGB:
                if not isinstance(color, int):
                    result = False
                    break
                elif color < 0 or color > 255:
                    result = False

            if result:
                return True

        print(self.__COLOR_INPUT_ERROR)
        return False

    def __is_valid_sides(self, *args):
        for side in args:
            if not isinstance(side, int | float):
                return False
            elif side <= 0:
                return False
        return True

    def __init__(self, color_RGB, *sides, filled=False):
        self.__sides = []
        self.__color = [0, 0, 0]
        self.__filled = filled

        self.set_sides(*sides)
        self.set_color(color_RGB)

    def __len__(self):
        return 0 if len(self.__sides) == 0 else sum(self.__sides)

    def __str__(self):
        return 'Class: {}, sides: {}, color: {}, perimeter: {}, square: {}, volume: {}'.format(
            self.__class__.__name__,
            self.__sides,
            self.__color,
            self.__len__(),
            self.get_square() if self.get_square() else self.__SHAPE_NOT_SET_ERROR,
            self.get_volume() if self.get_volume() else self.__SHAPE_NOT_SET_ERROR,
        )

    def set_color(self, color_RGB):
        if self.__is_valid_color(color_RGB):
            self.__color = color_RGB

    def set_sides(self, *sides):
        if self._required_sides_count and len(sides) != self._required_sides_count:
            return False

        if self.__is_valid_sides(*sides):
            self.__sides.clear()
            for side in sides:
                self.__sides.append(side)
            return True
        return False

    def get_sides(self):
        return self.__sides

    def get_color(self):
        return self.__color

    def get_square(self):
        return 0

    def get_volume(self):
        return 0


if __name__ == '__main__':
    figures = [
        Figure([100, 120, 220], 10, 10, 10, 10),
        Figure([100, 120, 220], 10, -10, 10, 10),
        Figure([100, -120, 220], 10, 10, 10, 10),
        Figure([100, 20, 220], 50)
    ]
    color = [50, 100, 150]
    invalid_color = [260, 10, 10]

    print(*figures, sep='\n', end='\n\n')
    figures[0].set_color(invalid_color)
    print(figures[0])
    figures[0].set_color(color)
    print(figures[0])

    figures[0].set_sides(5, 15, 48, 1)
    print('\n', figures[0])
    figures[0].set_sides(5, -15, 48, 1)
    print('\n', figures[0])
    figures[0].set_sides(5, '15', 48, 1)
    print('\n', figures[0])
