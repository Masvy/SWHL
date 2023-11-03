from sqlalchemy.orm import sessionmaker
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import and_f,  Command
from environs import Env

from keyboards.inline import admin_kb
from filters.admin_filters import IsAdmin
from database.admin import count_ids, count_fill_name, count_birthday, \
    count_stick_grip, count_photo, count_name, count_foundation, \
    count_arena, count_contact, count_number


admin_router: Router = Router()

env = Env()
env.read_env()


@admin_router.message(and_f(Command(commands='admin'),
                            IsAdmin(env('ADMIN_IDS'))))
async def start_admin(message: Message):
    await message.answer('Выбери действие:',
                         reply_markup=admin_kb)


@admin_router.callback_query(F.data == 'view_players')
async def show_players(callback: CallbackQuery,
                       session_maker: sessionmaker,
                       bot: Bot):
    ids = await count_ids(session_maker)
    full_name = await count_fill_name(session_maker)
    birthday = await count_birthday(session_maker)
    stick_grip = await count_stick_grip(session_maker)
    photo = await count_photo(session_maker)
    for i in range(len(ids)):
        await bot.send_photo(chat_id=callback.message.chat.id,
                             photo=photo[i],
                             caption=f'Имя игрока: {full_name[i]}\nДата '
                             f'рождения игрока: {birthday[i]}\n'
                             f'Хват клюшки: {stick_grip[i]}\n')


@admin_router.callback_query(F.data == 'views_commands')
async def show_commands(callback: CallbackQuery,
                        session_maker: sessionmaker):
    ids = await count_ids(session_maker)
    name = await count_name(session_maker)
    foundation = await count_foundation(session_maker)
    arena = await count_arena(session_maker)
    contact = await count_contact(session_maker)
    number = await count_number(session_maker)
    for i in range(len(ids)):
        await callback.message.answer(text=f'Название команды: {name[i]}\n'
                                      f'Дата основания: {foundation[i]}\n'
                                      f'Арена: {arena[i]}\nФИО контактного '
                                      f'лица: {contact[i]}\nНомер контактного '
                                      f'лица: {number[i]}')
