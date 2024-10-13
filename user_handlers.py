import os
from aiogram import Router, types
from service import get_weather
from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()

user_router = Router()


@user_router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Привет! Напиши название города, и я пришлю тебе сводку по погоде!")


@user_router.message()
async def get_weather_city(message: types.Message):
    city = message.text.strip()
    weather_data = get_weather(city, os.getenv('OPEN_WEATHER_TOKEN'))
    if weather_data:
        response = (
            f'Погода в городе {weather_data["city"]}\n'
            f'Температура: {weather_data["cur_weather"]}°C\n'
            f'Ощущается как: {weather_data["cur_weather_feels_like"]}°C\n'
            f'Описание: {weather_data["weather_description"]}\n'
            f'Влажность: {weather_data["humidity"]}%\n'
            f'Скорость ветра: {weather_data["wind_speed"]} м/с'
        )
        await message.answer(text=response)
    else:
        await message.answer(text='Проверьте название города!')
