"""
Задание:
Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.

Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег. Необходимо
использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.
"""
import time
from threading import Thread, Lock


class BankAccount:
    def __init__(self, balance=1000):
        self.__balance = balance
        self.__operation_lock = Lock()

    def deposit(self, amount):
        with self.__operation_lock:
            self.__balance += amount
            print(f'Deposited {amount}, new balance is {self.__balance}')

    def withdraw(self, amount):
        if amount > self.__balance:
            with self.__operation_lock:
                print('Not enough remaining funds')
            return 0

        with self.__operation_lock:
            self.__balance -= amount
            print(f'Withdrew  {amount}, new balance is {self.__balance}')
        return amount


def deposit_task(account, amount, delay=0, operations=5):
    for _ in range(operations):
        time.sleep(delay)
        account.deposit(amount)

def withdraw_task(account, amount, delay=0, operations=5):
    for _ in range(operations):
        time.sleep(delay)
        account.withdraw(amount)


account = BankAccount(10000)
delay = 0.000005
operations_count = 3000
deposit_thread = Thread(target=deposit_task, args=(account, 100, delay, operations_count))
withdraw_thread = Thread(target=withdraw_task, args=(account, 100, delay, operations_count))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

