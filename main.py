import requests
city = "Yakutsk"
language = "ru"
appid = "3ec53bf38002c6ec12cac9467e9817a9"

res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': language, 'APPID': appid})
data = res.json()
if not data:
    print('Мы не нашли такой город')
else:
    print("Город:", city)
    print("Скорость ветра:", data['wind']['speed'])
    print("Видимость:", data['visibility'])

'''
res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

for i in data['list']:
    print("Дата <", i['dt_txt'], ">")
    print("Скорость ветра:", i['wind']['speed'])
    print("Видимость:", i['visibility'])
    print("____________________________")
'''