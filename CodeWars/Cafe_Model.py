from threading import Thread, Lock
from time import sleep
from queue import Queue

class EnvObserver:
    def notify(self, time, customers_queue):
        pass

class Environment(Thread):
    __MIN_DELAY = 0.005
    __CUSTOMER_SPAWN_TIME = 10

    def __init__(self):
        super().__init__()
        self.__time = {'H': 0, 'M': 0, 'Sleep': self.__MIN_DELAY}
        self.__customers = Queue()
        self.__customers_not_spawned_mins = 0
        self.__observers = []

    def subscribe(self, observer):
        self.__observers.append(observer)

    def run(self):
        # while True:
        for _ in range(60 * 24):
            sleep(self.__MIN_DELAY)
            self.__customers_not_spawned_mins += 1
            self.__increase_time()
            self.__spawn_customer()
            for observer in self.__observers:
                observer.notify(self.__time, self.__customers)

    def get_customer(self):
        return self.__customers.get()

    def get_time(self):
        return self.__time['H'] * 24 + self.__time['M']

    def __increase_time(self):
        self.__time['M'] += 1
        if self.__time['M'] == 60:
            self.__time['M'] = 0
            self.__time['H'] += 1
            if self.__time['H'] == 24:
                self.__time['H'] = 0
        # print(f'{self.__time["H"]}:{self.__time["M"]}')

    def __spawn_customer(self):
        if 9 <= self.__time['H'] < 23 and self.__customers_not_spawned_mins > self.__CUSTOMER_SPAWN_TIME:
            customer = Customer()
            self.__customers.put(customer)
            print(f'{self.__time["H"]}:{self.__time["M"]} Customer # {customer.id} arrived')
            self.__customers_not_spawned_mins = 0


class Customer:
    customers_total_count = 0

    def __init__(self):
        Customer.customers_total_count += 1
        self.id = Customer.customers_total_count


class Table:
    def __init__(self):
        self.is_busy = False


class Cafe(EnvObserver):
    __SERVICE_TIME = 45
    __CLOSEOUT_TIME = {'H': 21, 'M': 0}

    def __init__(self, number_of_tables):
        self.__tables = [Table() for _ in range(number_of_tables)]
        self.__operation_lock = Lock()
        self.__current_time = {}

    def notify(self, time, customers_queue):
        self.__current_time = time

        if customers_queue.qsize() > 0:
            if self.__convert_time_to_mins(self.__CLOSEOUT_TIME) - self.__SERVICE_TIME * customers_queue.qsize() > \
                    self.__convert_time_to_mins(time):
                Thread(target=self.__serve_customer, args=(customers_queue.get(), )).start()
            else:
                return

    def __convert_time_to_mins(self, time):
        return time['H'] * 60 + time['M']

    # def start_service(self, customer):
    #     while True:
    #         customer = environment.get_customer()
    #         if self.__get_free_table():
    #             pass

    def __serve_customer(self, customer):
        while True:
            table = self.__get_free_table()
            if table:
                with self.__operation_lock:
                    table.is_busy = True

                start_time_min = self.__convert_time_to_mins(self.__current_time)
                current_time_min = start_time_min
                print(f'{self.__current_time["H"]}:{self.__current_time["M"]} Customer # {customer.id} service started')
                while start_time_min + self.__SERVICE_TIME > \
                        current_time_min:
                    sleep(self.__current_time['Sleep'])
                    current_time_min += 1

                print(f'{self.__current_time["H"]}:{self.__current_time["M"]} Customer # {customer.id} service ended')
                with self.__operation_lock:
                    table.is_busy = False

                return
            else:
                sleep(self.__current_time['Sleep'])


    def __get_free_table(self):
        with self.__operation_lock:
            for table in self.__tables:
                if not table.is_busy:
                    return table
            return 0


if __name__ == '__main__':
    environment = Environment()
    environment.start()
    cafe = Cafe(5)
    environment.subscribe(cafe)
    # cafe.start_service(environment)
