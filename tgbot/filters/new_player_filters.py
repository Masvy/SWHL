from datetime import datetime

from aiogram.types import Message
from aiogram.filters import BaseFilter


class IsBirthday(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        try:
            datetime.strptime(message.text, '%d.%m.%Y')
            return True
        except ValueError:
            return False
