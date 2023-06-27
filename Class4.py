import datetime as dt
import requests

def hello(name:str) -> str:
    print(f'Hello {name}')

for i in range(1,10):
    hello('Vlad')




# Type 1
def current_date():
    return dt.datetime.now()

print(current_date())

start  = current_date()
print(start)
s = 0
for i in range(0, 10000000):
    s += i
print(s)
end = current_date()
print(f'Start : {start} End : {end} \nTime: {end - start}')


def check_status_code(status_code: str) -> bool:
    match status_code:
        case 200: return True
        case 404: return False
        case _: return False



req = requests.get('https://api.monobank.ua/bank/currency')

print(req, req.status_code)

currency = {
    840: '💵',
    978: '💶'
}

if check_status_code(req):
    print('We can work with currency')
    for i in req.json():
        if i['currencyCodeA'] in (840, 978):
            print(f"Code is: {i['currencyCodeA']} Image: {currency[i['currencyCodeA']]} Buy: {i['rateBuy']}")
else:
    print(f'we can\'t work with currency {check_status_code(req)}')


tuple_4 = (1,2,3,4,5)
print(tuple_4, tuple_4.__sizeof__())

list_ = [1,2,3,4,5]
print(list_, list_.__sizeof__())


fruits = ("apple", "banana", "cherry", "melon")

# can use index
print(fruits[0])
print(fruits[2])

# collection can iterate
for fruit in fruits:
    print(fruit)

# Tuple unpacking
first_fruit, second_fruit, *remaining_fruits = fruits
print(first_fruit)        # Output: apple
print(second_fruit)       # Output: banana
print(remaining_fruits)   # Output: ['cherry', 'durian']

# Tuple concatenation - one more operation
more_fruits = ("elderberry", "fig")
all_fruits = fruits + more_fruits
print(all_fruits)




dict_1 = {} # create emp dict
dict_2 = dict() # create emp dict with system word
country = {
    'Ukraine': {'Kyiv': ('Teremku, Darn, Печерськ')},
    'Germany': 'Berlin',
    'UK': 'London',
}

print(f'Type: {type(dict_1)} Value: {dict_1} ')
print(f'Type: {type(dict_2)} Value: {dict_2} ')
print(f'Type: {type(country)} Value: {country} ')

# Dict - має внутрішні методи для виводу значеннь
print(country.items()) # Повертає ключ-значення пари
print(country.keys()) # Повертає ключі
print(country.values()) # Повертає значення


# Отримати значення із словника
print(country['Ukraine']) # Поверне помилку якщо ключа не має
print(country.get('Ukraine')) # Поверне null




country['New Country'] = 'New capital' # create new key - value

print(country)

назва = 15
print(назва)

#del country['New Country']
#print(country)


for key, value in country.items():
    print(key, value)