from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[str]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return str(message.from_user.id) in self.admin_ids
