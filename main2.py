import requests

def get_weather(city):
    api_key = '8e91616aeef56bb88bcbd0de9f85303c'    # Вводим ключ
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    data = response.json()
 #   for i in data:
  #      print('Ключ---',i, 'значение',data[i])

    if response.status_code == 200:
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']


        print(f"Погода в городе {city}: {temperature}°C,{weather_description},скорость ветра {wind_speed} м/с ")
    else:
        print(f"Ошибка при получении данных о погоде: {data['message']}")


city = input("Введите название города: ")
get_weather(city)

#Ключ--- coord значение {'lon': 44.6678, 'lat': 43.0367}
# Ключ--- weather значение [{'id': 500, 'main': 'Rain', 'description': 'небольшой дождь', 'icon': '10d'}]
# Ключ--- base значение stations
# Ключ--- main значение {'temp': 18.92, 'feels_like': 18.64, 'temp_min': 18.92, 'temp_max': 18.92, 'pressure': 1015, 'humidity': 68, 'sea_level': 1015, 'grnd_level': 929}
# Ключ--- visibility значение 10000
# Ключ--- wind значение {'speed': 3, 'deg': 30}
# Ключ--- rain значение {'1h': 0.33}
# Ключ--- clouds значение {'all': 75}
# Ключ--- dt значение 1750264594
# Ключ--- sys значение {'type': 1, 'id': 8969, 'country': 'RU', 'sunrise': 1750209700, 'sunset': 1750264996}
# Ключ--- timezone значение 10800
# Ключ--- id значение 473249
# Ключ--- name значение Владикавказ
# Ключ--- cod значение 200