from aiogram import types
from aiogram.filters import BaseFilter

class IsRegularMessage(BaseFilter):
  async def __call__(self, message: types.Message) -> bool:
    return message.text is not None and not message.text.startswith('/')