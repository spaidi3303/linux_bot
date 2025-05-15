import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import command
import error
import os
load_dotenv('secrets.env')
TOKEN = os.getenv('TOKEN')

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(
        error.router,
        command.router

    )
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Finish')