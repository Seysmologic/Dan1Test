import datetime
import time
import random
import functools

def even_odd(r_low: int, r_high: int):

    for number in range(r_low, r_high):
        if number % 2 == 0:
            print(f'{number} is Even')
        else:
            print(f'{number} is Odd')


print(even_odd(1, 11))


def is_prime(num_s):
    if num_s == 1:
        print(num_s, 'is not a prime number')
    elif num_s > 1:
        # checking factors
        for i in range(2, num_s):
            if num_s % i == 0:
                print(num_s, 'is not a prime number')
                break
        else:
            print(num_s, 'is a prime number')


print(is_prime(int(input('Enter number').strip())))


def arr_avr(arr_: list):
    if len(arr_) > 0:
        print(sum(arr_) / len(arr_))
    else:
        print('List is empty')


print(arr_avr([1, 5]))


def count_elem(elem, text: str):
    if elem in text:
        return f'"{elem}" is in text {text.count(elem)} times'
    else:
        print('Element is not in text')

print(count_elem('l', 'Hello World'))


timestamp = time.time()  # Поточний час
local_time = time.localtime(timestamp)  # Перетворення часу на локальний часовий пояс
print(local_time, type(local_time))
print(local_time.tm_year, local_time.tm_mday, local_time.tm_mon) # отримати складову часу за допомогою дот нотації

date1 = datetime.date(2023, 4, 10)
date2 = datetime.date(2024, 4, 30)

delta = date2 - date1  # Різниця між датами
print(delta.days, delta)  # Виведення кількості днів між датами


### Zip - Функція яка дозволяє поєднати два об'єкти в один
list1 = [1, 2, 3, 4,5]
list2 = ['a', 'b', 'c', 'd']

zipped = zip(list1, list2)  # Злиття списків
print(zipped, list(zipped))  # Виведення злитого ітерабельного об'єкту у вигляді списку


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['A', 'B', 'C']

zipped = zip(list1, list2, list3)  # Злиття списків
print(zipped, list(zipped))

# Map - примінити функцію для всіх
# map(function, iterable object) - загальна структура
numbers = [i for i in range(0, 15)]

def square(x: int) -> int:
    return x ** 2

sq = map(square, numbers)
print(numbers, list(sq), sq)

# Або використати функцію
sq1 = map(lambda x: x ** 2, numbers)
print(list(sq1))


# filter - filter(function, iterable object)

even = tuple(filter(lambda x: x % 2 == 0, numbers))
print(even)



from functools import reduce # потрібно імпортувати із built-in бібліотеки

numbers = [i for i in range(1, 6)]

product = reduce(lambda x, y: x+y, numbers)
print(product)  # 1 * 2 * 3 * 4 * 5
# 1 , 2 -> 2
# 2 , 3 -> 6
# etc...



list_str = ['1', '2', '3', '4', '5']
list_int = list(map(int, list_str))
print(list_int)


arr_ = [i for i in range(1, 101)]

even = list(filter(lambda x: x % 2 == 0, arr_))

print(even)

arr_mult = [i for i in range(1, 6)]

res_mult = functools.reduce(lambda x, y: x*y, arr_mult)
print(res_mult)


arr_num = [1, 2, 3, 4, 5]

arr_sq = map(lambda x: x**2, arr_num)


#task6
arr_sum = [i for i in range(1, 6)]

res_sum = functools.reduce(lambda x, y: x+y, arr_sum)
print(res_sum)

#task7

lis = ['apple', 'banana', 'cherry']

lis_len = list(map(lambda x: len(x), lis))

print(lis_len)

#task9
lis1 = [1, 5, 3, 9, 2]

print(functools.reduce(lambda a, b: a if a > b else b, lis1))
print(functools.reduce(lambda x, y: max(x, y), lis1))

#task10
lis = ['apple', 'banana', 'cherry']

lis_len = list(map(lambda x: x.upper(), lis))

print(lis_len)


#task6

arr_more_avg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr_avg = reduce(lambda x, y: x+y, arr_more_avg) / len(arr_more_avg)

print(list(filter(lambda x: x > arr_avg, arr_more_avg)))

