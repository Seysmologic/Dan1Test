from functools import reduce

#task1
def div_three(num: str):
    if num % 3 == 0:
        return True
    else:
        return False


print(div_three(8))

#task2


def leap_year(year: int) -> str:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, 'is a Leap Year')
    else:
        print(year, 'is not a Leap Year')


print(leap_year(1991))


#task3
def triangle(a: int, b: int, c: int):
    if a == b == c:
        return 'Equilateral Triangle'
    elif a == b or b == c or c == a:
        return 'Isosceles Triangle'
    else:
        return 'Scalene Triangle'

print(triangle(1, 2, 1))


#task5

def vowel_chk(letter: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False



print(vowel_chk('a'))


#task 6

def triangle2(a: int, b: int, c: int):
    return True if (a * a + b * b == c * c) or (c * c + b * b == a * a) or (a * a + c * c == b * b) else False

print(triangle2(3, 4, 5))


#task4

def century_chk(year: int):
    return True if year % 100 == 0 else False

print(century_chk(200))



# --------------------------------------------------------------------------------------------------------


#task1

def func1():
    pass

#task1
arr_ = []

def func1(a: int, b: int):

    numbers = [i for i in range(a, b)]
    if a < b:
        for i in numbers:
            if i % 2 == 0:
                arr_.append(i)
        print(arr_)

print(func1(int(input('Start:').strip()), int(input('Finish:').strip())))

def func1(a: int, b: int):

    numbers = [i for i in range(a, b+1)]
    return reduce(lambda x, y: x * y, numbers)


print(func1(int(input('Start:').strip()), int(input('Finish:').strip())))








#task3
def func1():
    pass

#task4
def func1():
    pass

#task5
