""""
file = open('Japan.txt', 'w')

file.write('Capital: Tokyo\nPopulation: 120_000_00')

file.close()


file = open('UK.txt', 'w')

file.write('Capital: London\nPopulation: 90_0000')

file.close()


with open("Japan.txt", 'r') as file, open("UK.txt", 'r') as file1:
    data = file.read()
    print(data)
    print(file1.read())

with open("first_file.txt", 'a') as file:
    file.write('\nAdd new line of code')

    """

# Weather App
import requests

API_KEY = "33d99a1c99c5ea82e6aaff8592cd6fc3"

city = input('Enteryou city: ').strip().capitalize()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}" # &units=metric

response = requests.get(url)

print(response.status_code, response) # відповідь сервера, від 1xx до 5xx


if response.status_code == 200:
    data = response.json()
    print(data, data.keys())

    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    print(f"Погода в місті {city}: {description}")
    print(f"Температура: {temp}°C, відчувається як {feels_like}°C")
else:
    print("Не вдалося отримати дані про погоду")

data = response.json()
print(data)

print(data['main']['temp'])