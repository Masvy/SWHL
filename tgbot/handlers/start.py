from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from lexicon.users_lexicon import MENU

start_router: Router = Router()


@start_router.message(CommandStart())
async def show_menu(message: Message):
    await message.answer(text=MENU['commands_list'])