from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

from lexicon.users_lexicon import BASIC_COMMANDS
from keyboards.inline import partners_k

start_router: Router = Router()


@start_router.message(CommandStart())
async def show_menu(message: Message):
    await message.answer(text=BASIC_COMMANDS['commands_list'])


@start_router.message(Command(commands='leaguedescription'))
async def show_league_description(message: Message):
    photo = FSInputFile('tgbot/photo/О лиге.PNG')
    await message.answer_photo(photo=photo)
    await message.answer(text=BASIC_COMMANDS['league_description'])


@start_router.message(Command(commands='ourpartners'))
async def show_partners(message: Message):
    await message.answer(text=BASIC_COMMANDS['our_partners'],
                         reply_markup=partners_k)
