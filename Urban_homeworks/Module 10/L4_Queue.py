"""
Задание:
Моделирование работы сети кафе с несколькими столиками и потоком посетителей, прибывающих для заказа пищи и
уходящих после завершения приема.

Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют еду и уходят.
Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в очередь на ожидание.
"""


from threading import Thread, Lock
from queue import Queue
from time import sleep


class Table:
    def __init__(self, table_number):
        self.number = table_number
        self.is_busy = False


class Cafe:
    __CUSTOMER_ARRIVAL_DELAY = 0.1
    __QUEUE_CHECK_DELAY = __CUSTOMER_ARRIVAL_DELAY / 19
    __CUSTOMER_SERVICE_TIME = 0.5
    __NO_MORE_CUSTOMERS_EXPECTED = __CUSTOMER_ARRIVAL_DELAY * 3

    __operation_lock = Lock()

    def __init__(self, tables):
        if not isinstance(tables, list | tuple):
            raise TypeError('Tables list required!')

        if len(tables) == 0:
            raise ValueError('Can\'t work without tables!')

        self.customers_queue = Queue()
        self.tables = tables
        self.customers_not_arrived_time = 0

        Thread(target=self.start_service).start()

    def customer_arrival(self, customer_count_limit=20):
        customer_number = 1
        while customer_number <= customer_count_limit:
            customer = Customer(customer_number)
            with self.__operation_lock:
                self.customers_not_arrived_time = 0
                self.customers_queue.put(customer)
                print(f'Посетитель номер {customer_number} прибыл.')

            if self.customers_queue.qsize() > 1 or not self.__get_free_table():
                with self.__operation_lock:
                    print(f'Посетитель номер {customer.number} ожидает свободный стол.')

            customer_number += 1
            sleep(self.__CUSTOMER_ARRIVAL_DELAY)

    def __get_free_table(self):
        with self.__operation_lock:
            for table in self.tables:
                if not table.is_busy:
                    return table
        return 0

    def serve_customer(self, customer, table):
        with self.__operation_lock:
            table.is_busy = True
            print(f'Посетитель номер {customer.number} сел за стол {table.number},')

        sleep(self.__CUSTOMER_SERVICE_TIME)
        with self.__operation_lock:
            table.is_busy = False
            print(f'Посетитель номер {customer.number} покушал и ушёл.')

    def start_service(self):
        while self.customers_not_arrived_time < self.__NO_MORE_CUSTOMERS_EXPECTED or not self.customers_queue.empty():
            free_table = self.__get_free_table()
            if free_table and not self.customers_queue.empty():
                with self.__operation_lock:
                    Thread(target=self.serve_customer, args=(self.customers_queue.get(), free_table)).start()

            sleep(self.__QUEUE_CHECK_DELAY)
            self.customers_not_arrived_time += self.__QUEUE_CHECK_DELAY


class Customer:
    def __init__(self, number):
        self.number = number


tables = [
    Table(1),
    Table(2),
    Table(3)
]

cafe = Cafe(tables)
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
