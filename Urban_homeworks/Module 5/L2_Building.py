class Building:
    total = 0

    def __init__(self, number_of_floors=0, building_type='жилое'):
        self.number_of_floors = number_of_floors
        self.building_type = building_type
        Building.total += 1

    def __eq__(self, other):
        return self.building_type == other.building_type and self.number_of_floors == other.number_of_floors

    def __str__(self):
        return f'Тип здания: {self.building_type}, этажей: {self.number_of_floors}'


if __name__ == '__main__':
    # first_building = Building(5)
    # second_building = Building(5)
    # print(f'{first_building == second_building} {first_building is second_building}')
    # second_building.number_of_floors = 7
    # print(first_building == second_building)

    for i in range(40):
        print(Building(i + 1))

    print(f'Всего потсроено зданий: {Building.total}')
