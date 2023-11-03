import aiohttp
import datetime

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, InputMediaPhoto, \
    CallbackQuery

from utils.comm_scraping import commands, urls
from lexicon.users_lexicon import BASIC_COMMANDS
from keyboards.inline import partners_kb, our_links_kb, stickers_kb, \
    statistics_kb

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


@start_router.message(Command(commands='stickers'))
async def send_stickers(message: Message):
    await message.answer(text=BASIC_COMMANDS['take_stickers'],
                         reply_markup=stickers_kb)


@start_router.message(Command(commands='countdown'))
async def count_time(message: Message):
    date = datetime.datetime(2024, 4, 21) - datetime.datetime.now()
    await message.answer(f'Конец сезона 2023/2024 через {date.days} дней, '
                         f'{date.seconds // 3600} часов,'
                         f'{(date.seconds // 60) % 60} минут.')


@start_router.message(Command(commands='commands'))
async def show_commands(message: Message):
    async with aiohttp.ClientSession() as session:
        url = 'https://swhl.ru/tournament/1033299/tables'
        commands_list = await commands(url, session)
        url_list = await urls(url, session)
        html_commands = []
        for command, link in zip(commands_list[:8], url_list[:8]):
            html_commands.append(f'<a href="{link}">{command}</a>')
        html_message = '\n\n'.join(html_commands)
        await message.answer(f'Наши команды:\n{html_message}')


@start_router.message(Command(commands='player_statistics'))
async def show_statistics(message: Message):
    await message.answer('Веберите категорию:',
                         reply_markup=statistics_kb)


@start_router.callback_query(F.data == 'sniper_pressed')
async def show_sniper(callback: CallbackQuery):
    photo = FSInputFile(
        '/home/nikita/Рабочий стол/SWHL/tgbot/pictures/sniper.png')
    await callback.message.answer_photo(photo)


@start_router.callback_query(F.data == 'assists_pressed')
async def show_assists(callback: CallbackQuery):
    photo = FSInputFile(
        '/home/nikita/Рабочий стол/SWHL/tgbot/pictures/assists.png')
    await callback.message.answer_photo(photo)


@start_router.callback_query(F.data == 'goalpas_pressed')
async def show_goalpas(callback: CallbackQuery):
    photo = FSInputFile(
        '/home/nikita/Рабочий стол/SWHL/tgbot/pictures/goalpas.png')
    await callback.message.answer_photo(photo)


@start_router.callback_query(F.data == 'penalties_pressed')
async def show_penalties(callback: CallbackQuery):
    photo = FSInputFile(
        '/home/nikita/Рабочий стол/SWHL/tgbot/pictures/penalties.png')
    await callback.message.answer_photo(photo)


@start_router.callback_query(F.data == 'best_pressed')
async def show_best(callback: CallbackQuery):
    photo = FSInputFile(
        '/home/nikita/Рабочий стол/SWHL/tgbot/pictures/best.png')
    await callback.message.answer_photo(photo)


@start_router.callback_query(F.data == 'goalkeepers_pressed')
async def show_goalkeepers(callback: CallbackQuery):
    photo = FSInputFile(
        '/home/nikita/Рабочий стол/SWHL/tgbot/pictures/goalkeepers.png')
    await callback.message.answer_photo(photo)


@start_router.callback_query(F.data == 'saltworts_pressed')
async def show_saltworts(callback: CallbackQuery):
    photo = FSInputFile(
        '/home/nikita/Рабочий стол/SWHL/tgbot/pictures/saltworts.png')
    await callback.message.answer_photo(photo)


@start_router.callback_query(F.data == 'teams_pressed')
async def show_teams(callback: CallbackQuery):
    photo = FSInputFile(
        '/home/nikita/Рабочий стол/SWHL/tgbot/pictures/teams.png')
    await callback.message.answer_photo(photo)
