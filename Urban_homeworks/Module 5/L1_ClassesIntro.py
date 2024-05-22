class House:
    def __init__(self, number_of_floors):
        self.number_of_floors = number_of_floors
        self.current_floor = 0


    def examine_floors(self):
        if self.number_of_floors <= 0:
            print('Еще не построен')
        else:
            while self.current_floor < self.number_of_floors:
                self.current_floor += 1
                print(f'Поднялись на 1 этаж, Текущий этаж: {self.current_floor}')


new_house = House(10)
new_house.examine_floors()