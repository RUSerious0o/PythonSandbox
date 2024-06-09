from Figure import Figure


class Cube(Figure):
    _required_sides_count = 1

    def __init__(self, color_RGB, cube_edge, filled=False):
        super().__init__(color_RGB, 0, filled)
        self.__edge = 0

        self.set_sides(cube_edge)

    def __len__(self):
        p = super().get_sides()
        if p:
            return p[0] * 12
        else:
            return 0

    def get_volume(self):
        return self.__edge ** 3

    def set_sides(self, *sides):
        if super().set_sides(*sides):
            self.__edge = sides[0]
            return True
        else:
            return False

    def get_sides(self):
        return super().get_sides() * 12

    def get_square(self):
        H = super().get_sides()
        if H:
            return H[0] ** 2 * 6
        else:
            return 0


if __name__ == '__main__':
    cubes = [
        Cube([10, 10, 10], 5, True),
        Cube([10, 10, 10], -5, True),
        Cube([10, 10, 10], 12)
    ]

    print(*cubes, sep='\n')
