import asyncio
import logging
from aiogram import Bot, Dispatcher
import error

users_try = {}
TOKEN = '8043533102:AAHj8BfINsY0coORH92wr5nWbNQ0s_7HOaM'

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(
        error.router

    )
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Finish')