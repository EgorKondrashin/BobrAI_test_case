import asyncio
import os
import requests
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from user_handlers import user_router


async def main() -> None:

    load_dotenv()
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()

    dp.include_router(user_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
