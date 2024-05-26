class Building:
    def __init__(self, number_of_floors=0, building_type='жилое'):
        self.number_of_floors = number_of_floors
        self.building_type = building_type

    def __eq__(self, other):
        return self.building_type == other.building_type and self.number_of_floors == other.number_of_floors


if __name__ == '__main__':
    first_building = Building(5)
    second_building = Building(5)
    print(f'{first_building == second_building} {first_building is second_building}')
    second_building.number_of_floors = 7
    print(first_building == second_building)

