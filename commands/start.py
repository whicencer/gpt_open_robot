from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart

from utils import get_translation
from database import Database

start_router = Router()
db = Database()

@start_router.message(CommandStart())
async def start_command_handler(message: Message) -> None:
  if not db.check_is_user_exists(message.from_user.id):
    db.create_new_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name, message.from_user.language_code, message.from_user.is_premium)
  await message.answer(get_translation("start_greeting", message.from_user.language_code))