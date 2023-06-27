# Division by 3 and 5. if statement

number = int(input('Enter the number: ').strip())
# moving through conditions
if number % 3 == 0 and number % 5 == 0:
    print('ham')
elif number % 3 == 0:
    print('foo')
elif number % 5 == 0:
    print('bar')
else:
    print(f'5 and 3 are not factors of the {number}')


# Checking for the bigger number
try:
    number_a = int(input('Enter the number A: ').strip())
    number_b = int(input('Enter the number B: ').strip())
    if number_a > number_b:
        print(f'{number_a} is greater than {number_b}')
    elif number_a < number_b:
        print(f'{number_b} is greater than {number_a}')
    else:
        print('Numbers are equal')
except ValueError:
    print('You have to enter int number')


# Checking status of three numbers in array

list_of_three = [3, 4, 6]
list_of_three.sort()  # sorting list in ascending order
print(f'{list_of_three[0]} is the smallest number\n{list_of_three[2]} is the biggest number\n'
      f'{list_of_three[1]} is just average')


# Fizz Buzz? o.O

arr_fb = [i for i in range(1, 101)]
for i in arr_fb:
    if i % 3 == 0 and i % 5 == 0:
        index_fb = arr_fb.index(i)  # taking index of the element
        arr_fb[index_fb] = 'Fizz Buzz'   # replacing item under that index in the list
    elif i % 3 == 0:
        index_fb = arr_fb.index(i)
        arr_fb[index_fb] = 'Fizz'  # pycharm is unhappy with this approach. Any idea why?
    elif i % 5 == 0:
        index_fb = arr_fb.index(i)
        arr_fb[index_fb] = 'Buzz'
print(list(map(str, arr_fb)))  # transforming items in list into str for convenience (might be redundant?)


# Exploding 7

arr_boom = [i for i in range(1, 101)]
for i in arr_boom:
    if i % 7 == 0:
        index_boom = arr_boom.index(i)  # taking index of the element
        arr_boom[index_boom] = 'Boom'   # replacing item under that index in the list
    if str(7) in str(i) and i % 7 != 0:
        index_boom = arr_boom.index(i)  # taking index of the element
        arr_boom[index_boom] = 'Boom'   # replacing item under that index in the list
print(list(map(str, arr_boom)))  # transforming items in list into str for convenience (might be redundant?)
