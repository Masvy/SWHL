from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

from lexicon.users_lexicon import BASIC_COMMANDS
from keyboards.inline import partners_k, our_links

start_router: Router = Router()


@start_router.message(CommandStart())
async def show_menu(message: Message):
    await message.answer(text=BASIC_COMMANDS['commands_list'])


@start_router.message(Command(commands='league_description'))
async def show_league_description(message: Message):
    photo = FSInputFile('tgbot/photo/О лиге.PNG')
    await message.answer_photo(photo=photo)
    await message.answer(text=BASIC_COMMANDS['league_description'])


@start_router.message(Command(commands='our_partners'))
async def show_partners(message: Message):
    await message.answer(text=BASIC_COMMANDS['our_partners'],
                         reply_markup=partners_k)


@start_router.message(Command(commands='our_links'))
async def show_links(message: Message):
    await message.answer(text=BASIC_COMMANDS['our_links'],
                         reply_markup=our_links)


@start_router.message(Command(commands='offer_partners'))
async def show_offer(message: Message):
    photo = FSInputFile('tgbot/photo/Предложения для партнеров.PNG')
    await message.answer_photo(photo=photo,
                               caption=BASIC_COMMANDS['our_mail'])
