from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, InputMediaPhoto

from lexicon.users_lexicon import BASIC_COMMANDS
from keyboards.inline import partners_kb, our_links_kb, stickers_kb

start_router: Router = Router()


@start_router.message(CommandStart())
async def show_menu(message: Message):
    await message.answer(text=BASIC_COMMANDS['commands_list'])


@start_router.message(Command(commands='league_description'))
async def show_league_description(message: Message):
    photo = FSInputFile('tgbot/pictures/О лиге.PNG')
    await message.answer_photo(photo=photo)
    await message.answer(text=BASIC_COMMANDS['league_description'])


@start_router.message(Command(commands='our_partners'))
async def show_partners(message: Message):
    await message.answer(text=BASIC_COMMANDS['our_partners'],
                         reply_markup=partners_kb)


@start_router.message(Command(commands='our_links'))
async def show_links(message: Message):
    await message.answer(text=BASIC_COMMANDS['our_links'],
                         reply_markup=our_links_kb)


@start_router.message(Command(commands='offer_partners'))
async def show_offer_partners(message: Message):
    photo = FSInputFile('tgbot/pictures/Предложения для партнеров.PNG')
    await message.answer_photo(photo=photo,
                               caption=BASIC_COMMANDS['our_mail'])


@start_router.message(Command(commands='offer_participate'))
async def show_offer_participate(message: Message):
    picture_1 = InputMediaPhoto(type='photo',
                                media=FSInputFile('tgbot/pictures/слайд1.png'))
    picture_2 = InputMediaPhoto(type='photo',
                                media=FSInputFile('tgbot/pictures/слайд2.png'))
    picture_3 = InputMediaPhoto(type='photo',
                                media=FSInputFile('tgbot/pictures/слайд3.png'))
    media = [picture_1, picture_2, picture_3]
    await message.answer_media_group(media=media)
    await message.answer(text=BASIC_COMMANDS['offer_participate'])


@start_router.message(Command(commands='location'))
async def show_location(message: Message):
    picture_1 = InputMediaPhoto(type='photo',
                                media=FSInputFile('tgbot/pictures/комплекс.png'))
    picture_2 = InputMediaPhoto(type='photo',
                                media=FSInputFile('tgbot/pictures/преимущества.png'))
    media = [picture_1, picture_2]
    await message.answer(text=BASIC_COMMANDS['our_address'])
    await message.answer_location(latitude=55.79849300356317,
                                  longitude=37.60864468694828)
    await message.answer(text=BASIC_COMMANDS['our_arena'])
    await message.answer_media_group(media=media)


@start_router.message(Command(commands='stickers'))
async def send_stickers(message: Message):
    await message.answer(text=BASIC_COMMANDS['take_stickers'],
                         reply_markup=stickers_kb)
