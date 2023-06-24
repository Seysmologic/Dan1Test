import random

# Enter name assign random salary in a range of 1000 - 10000 print the result
name = input("Enter your name: ").strip().capitalize()
salary = random.randint(1000, 10000)
print(f"{name} yearly salary is {round(salary * 12 // 1000)} thousand dollars")

# Taking random number and running through the query
rand_num = random.randint(1, 2000)
print(100 < rand_num < 999 and rand_num % 2 == 0)

# Taking random number and reversing it
print(str(rand_num)[::-1])

# Taking two random numbers and performing actions
rand_a = random.randint(1, 999)
rand_b = random.randint(1, 999)

print(f'a + b = {rand_a + rand_b} \na - b = {rand_a - rand_b} \na * b = {rand_a * rand_b} \na / b = {rand_a / rand_b}'
      f'\na % b = {rand_a % rand_b}')
