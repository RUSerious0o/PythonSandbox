from datetime import datetime
from pprint import pprint
from multiprocessing import Pool


class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request: tuple):
        if not isinstance(request, tuple | list):
            raise TypeError('request must be tuple(name, req_type, volume)')

        if not request[0] in self.data.keys():
            self.data[request[0]] = 0

        if request[1] == 'receipt':
            self.data[request[0]] += request[2]

        if request[1] == 'shipment':
            remains = self.data[request[0]]
            if request[2] <= remains:
                self.data[request[0]] -= request[2]

    def run(self, requests):
        [self.process_request(request) for request in requests]


def time_estimate(func):
    def wrapper(*args):
        start = datetime.now()
        func(*args)
        print(f'Estimated time: {datetime.now() - start}')

    return wrapper


def generate_requests(thrash_arg, number_of_reqs=1_250_000):
    from random import randint, choice

    prod_names = (
        'Гвозди',
        'Доска',
        'Блок',
        'Саморез',
        'Дюбель',
        'Швеллер',
        'Профиль',
        'Плитка',
        'Розетка'
    )
    req_types = (
        'receipt',
        'shipment'
    )

    requests = [(choice(prod_names), choice(req_types), randint(30, 250)) for _ in range(number_of_reqs)]
    # manager_dict
    return requests


if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)

    # additional test
    print()
    managers = (
        WarehouseManager(),
    )

    requests = []
    start = datetime.now()
    with Pool(processes=4) as pool:
        result = pool.map(generate_requests, range(4))

    for list_ in result:
        requests.extend(list_)
    print(f'Нагенерили {len(requests)} запросов за {datetime.now() - start} сек')

    time_estimate(managers[0].run)(requests)
    pprint(managers[0].data)
