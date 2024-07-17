import json
from datetime import datetime
from pprint import pprint
from time import sleep
from threading import Lock, Thread


class WarehouseManager:
    def __init__(self):
        self.data = {}
        self.operation_lock = Lock()

    def process_request(self, request: tuple):
        if not isinstance(request, tuple | list):
            raise TypeError('request must be tuple(name, req_type, volume)')

        if not request[0] in self.data.keys():
            with self.operation_lock:
                self.data[request[0]] = 0

        if request[1] == 'receipt':
            with self.operation_lock:
                self.data[request[0]] += request[2]

        if request[1] == 'shipment':
            remains = self.data[request[0]]
            if request[2] <= remains:
                with self.operation_lock:
                    self.data[request[0]] -= request[2]
                return request[2]

        # print(request, self.data)

    def run(self, requests):
        [self.process_request(request) for request in requests]

    def run_single_thread(self, requests):
        [self.process_request(request) for request in requests]


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
    from multiprocessing import Process

    print()
    managers = (
        WarehouseManager(),
        WarehouseManager()
    )
    requests = []


    def time_estimate(func):
        def wrapper(*args):
            start = datetime.now()
            func(*args)
            print(f'Estimated time: {datetime.now() - start}')

        return wrapper


    def generate_requests(number_of_reqs):
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

        return [(choice(prod_names), choice(req_types), randint(10, 250)) for _ in range(number_of_reqs)]


    requests = generate_requests(5_000_000)
    # Process(target=generate_requests, args=(1,)).start()

    time_estimate(managers[0].run_single_thread)(requests)
    time_estimate(managers[1].run)(requests)

    pprint(managers[0].data)
    pprint(managers[1].data)
    print(managers[0].data == managers[1].data)

"""
Постановка задачи, мягко говоря, странная:
Во-первых, задача на 'мультипроцессорность' подразумевает использование, например, Pool-а, А он, в свою очередь,
создает копии метода, которые ему скормили, для разных процессов. Т.е. все процессы, которые наплодит Пул, 
будут иметь общий доступ к iterable объекту, содержащему исходные данные для функции, но не к общему ресурсу для
складывания результатов работы. Ну и на threading.Lock он ругается. Таким образом это задание на многопоточность, 
а не на многопроцессность
Во-вторых, мы моделируем работу склада. А на складе, вообще-то, есть разница, в каком порядке грузы поступают и 
отгружаются. Если мы каждый поступающий запрос будем просто скармливать новому потоку, то при больших количествах 
запросов и отсутствии задержек выполнения, из-за GIL-а мы не сможем контролировать порядок их выполнения нашим 
менеджером и, следовательно, результат ...  
"""
