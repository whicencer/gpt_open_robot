import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from database import Database
from commands.start import start_router

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")

db = Database()
dp = Dispatcher()

async def main():
  bot = Bot(token=bot_token)
  
  dp.include_router(start_router)
  await dp.start_polling(bot)

if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  asyncio.run(main())