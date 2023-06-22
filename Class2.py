x = list(map(str, [input('Car manufacturer'), input('Year'), input('Engine')]))

print(f'Car manufacturer is {x[0]} \nManufactured in {x[1]} \nEngine type is {x[2]}')

print('Car manufacturer is', x[0], '\nManufactured in', x[1], '\nEngine type is', x[2])

x.append('100$')
print(x)
