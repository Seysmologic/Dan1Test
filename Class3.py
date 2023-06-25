from random import randint
import math
status_code = '200'
match status_code:
    case '200':
        print('OK')
    case '404':
        print('Error')
#    case ''


a = 0
while a < 3:
    print(a)
    a += 1

a = 0
while True:
    if a == 3:
        break
    else:
        print(a)
        a += 1


number = [i for i in range(randint(1, 100), randint(200, 500))]
# print(number)
x = []
for i in number:
    if i % 2 != 0:
        continue
    else:
        x.append(int(i))
print(x)


list_num = []

while len(list_num) <= 9:
    list_num.append(randint(1, 10))
print(list_num)

list_2 = []

for i in range(10):
    list_2.append(randint(1, 10))
print(list_2)


#arr_num = []

#while len(arr_num) < 10:
#    arr_num.append(float(input('Enter real number: ')))

#print(math.fsum(arr_num) / len(arr_num))

arr_num1 = []
while len(arr_num1) < 10:
    arr_num1.append(randint(1, 10))
print(sum(arr_num1) / len(arr_num1))


is_prime = int(input('Enter the number: '))
# first check for prime number
if is_prime == 1:
    print(is_prime, 'is not a prime number')
elif is_prime > 1:
    # checking factors
    for i in range(2, is_prime):
        if is_prime % i == 0:
            print(is_prime, 'is not a prime number')
            break
    else:
        print(is_prime, 'is a prime number')

is_prime2 = []
prime_2 = [i for i in range(1, 10)]
print(prime_2)
# first check for prime number
for i in prime_2:
    if i == 1:
        print(i)
        continue
    for factor in range(2, i):
        if i % factor != 0:
            print(i)
            is_prime2.append(i)
print(is_prime2)

