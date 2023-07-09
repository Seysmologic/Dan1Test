from functools import *
import time


class Rectangle:
    """
    Клас Rectangle представляє прямокутник з атрибутами width та height.

    :ivar width: Ширина прямокутника.
    :vartype width: float
    :ivar height: Висота прямокутника.
    :vartype height: float
    """
    def __init__(self, width, height):
        """
        Конструктор класу Rectangle.

        :param width: Ширина прямокутника.
        :type width: float
        :param height: Висота прямокутника.
        :type height: float
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Метод area обчислює площу прямокутника.

        :return: Площа прямокутника.
        :rtype: float
        """
        return self.width * self.height

    def perimeter(self):
        """
        Метод perimeter обчислює периметр прямокутника.

        :return: Периметр прямокутника.
        :rtype: float
        """
        return 2 * (self.width + self.height)


class Rect:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def per(self):
        return 2 * self.height + 2 * self.width

    def area(self):
        return self.height * self.width




sq1 = Rect(4, 8)
print(sq1.per())

cash_ = int(input('Enter the amount'))

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def add_balance(self):
        return self.balance + cash_

    def withdraw_balance(self):
        if self.balance > cash_:
            return self.balance - cash_
        else:
            return 'Not enough money'

    def __str__(self):
        return f'Account {self.account_number} has {self.balance}$ on its balance'

user1 = BankAccount(10008000, 1000)
print(user1.withdraw_balance())
print(user1.__str__())




def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper


@timer
def create_list(number: int = 1000000) -> list:
    return [i for i in range(1, number)] if isinstance(number, int) else []


sum(create_list())