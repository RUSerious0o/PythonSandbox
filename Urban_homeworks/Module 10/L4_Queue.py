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
    __QUEUE_CHECK_DELAY = 0.01
    __CUSTOMER_ARRIVAL_DELAY = 0.1
    __CUSTOMERS_COUNT_LIMIT = 20
    __CUSTOMER_SERVICE_TIME = 0.5

    __operation_lock = Lock()

    def __init__(self, tables):
        if not isinstance(tables, list | tuple):
            raise TypeError('Tables list required!')

        self.customers_queue = Queue()
        self.tables = tables

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= self.__CUSTOMERS_COUNT_LIMIT:
            sleep(self.__CUSTOMER_ARRIVAL_DELAY)
            customer = Customer(customer_number)
            with self.__operation_lock:
                self.customers_queue.put(customer)
                print(f'Посетитель номер {customer_number} прибыл.')

            customer_number += 1
            thread = Thread(target=self.__serve_customer, args=(customer, ))
            thread.start()


    def __serve_customer(self, customer):
        while True:
            for table in tables:
                if not table.is_busy:
                    table.is_busy = True
                    print(f'Посетитель номер {customer.number} сел за стол {table.number}. (начало обслуживания)')
                    sleep(self.__CUSTOMER_SERVICE_TIME)
                    print(f'Посетитель номер {customer.number} покушал и ушёл. (конец обслуживания)')
                    table.is_busy = False
                    return
            sleep(self.__QUEUE_CHECK_DELAY)


    def __serve_customers(self):
        while True:

            sleep(self.__QUEUE_CHECK_DELAY)

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
# customer_arrival_thread.join()