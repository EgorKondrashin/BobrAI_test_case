import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather(city: str, token: str):
    url = f'http://ru.api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric&lang=ru'
    response = requests.get(url)
    data = response.json()

    if data['cod'] != '404':
        return {
            'city': data['name'],
            'cur_weather': data['main']['temp'],
            'cur_weather_feels_like': data["main"]["feels_like"],
            'weather_description': data["weather"][0]["description"],
            'humidity': data["main"]["humidity"],
            'wind_speed': data["wind"]["speed"]
        }
    else:
        return


def main():
    city = input('Введите город: ')
    get_weather(city, os.getenv('OPEN_WEATHER_TOKEN'))


if __name__ == '__main__':
    main()
