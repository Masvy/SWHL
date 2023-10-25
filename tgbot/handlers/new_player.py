from aiogram import Router, F, types
from sqlalchemy.orm import sessionmaker
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter, and_f

from keyboards.inline import players_kb
from states.users_states import NewPlayer
from lexicon.users_lexicon import NEW_PLAYER
from filters.new_player_filters import IsBirthday
from database.players import add_user_id, add_name, add_birthday, \
    add_stick_grip, add_photo


player_router: Router = Router()


@player_router.callback_query(F.data == 'wrong')
@player_router.message(Command(commands='new_player'),
                       StateFilter(default_state))
async def start_new_player(update: types.Update, state: FSMContext):
    if isinstance(update, types.CallbackQuery):
        await update.message.answer(text=NEW_PLAYER['full_name'])
        await state.set_state(NewPlayer.full_name)
    else:
        await update.answer(text=NEW_PLAYER['full_name'])
        await state.set_state(NewPlayer.full_name)


@player_router.message(StateFilter(NewPlayer.full_name),
                       and_f(lambda x: x.text.replace(' ', 'a').isalpha(),
                       lambda x: x.text.count(' ') == 1 or
                       x.text.count(' ') == 2))
async def save_full_name(message: Message, state: FSMContext):
    await message.answer(text=NEW_PLAYER['birthday'])
    await state.update_data(full_name=message.text)
    await state.set_state(NewPlayer.birthday)


@player_router.message(StateFilter(NewPlayer.full_name))
async def wrong_full_name(message: Message):
    await message.answer(text=NEW_PLAYER['wrong_name'])


@player_router.message(StateFilter(NewPlayer.birthday),
                       IsBirthday())
async def save_birthday(message: Message, state: FSMContext):
    await message.answer(text=NEW_PLAYER['stick_grip'])
    await state.update_data(birthday=message.text)
    await state.set_state(NewPlayer.stick_grip)


@player_router.message(StateFilter(NewPlayer.birthday))
async def wrong_birthday(message: Message):
    await message.answer(text=NEW_PLAYER['wrong_birthday'])


@player_router.message(StateFilter(NewPlayer.stick_grip),
                       lambda x: x.text.lower() == 'левый' or
                       x.text.lower() == 'правый')
async def save_stick_grip(message: Message, state: FSMContext):
    await message.answer(text=NEW_PLAYER['photo'])
    await state.update_data(stick_grip=message.text)
    await state.set_state(NewPlayer.photo)


@player_router.message(StateFilter(NewPlayer.stick_grip))
async def wrong_stick_grip(message: Message):
    await message.answer(text=NEW_PLAYER['wrong_stick_grip'])


@player_router.message(StateFilter(NewPlayer.photo),
                       F.photo)
async def save_photo(message: Message,
                     state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    await message.answer(text=f'ФИО: {data["full_name"]}\nДата '
                         f'рождения: {data["birthday"]}\nХват '
                         f'клюшки: {data["stick_grip"]}\n\n'
                         'Проверьте, все ли данные верны?',
                         reply_markup=players_kb)


@player_router.callback_query(F.data == 'right')
async def save_data(callback: CallbackQuery,
                    state: FSMContext,
                    session_maker: sessionmaker):
    data = await state.get_data()
    await add_user_id(session_maker, callback.from_user.id)
    await add_name(session_maker, callback.from_user.id, data['full_name'])
    await add_birthday(session_maker, callback.from_user.id, data['birthday'])
    await add_stick_grip(session_maker, callback.from_user.id,
                         data['stick_grip'])
    await add_photo(session_maker, callback.from_user.id, data['photo'])
    await callback.message.edit_text(text=NEW_PLAYER['data_saved'])
    await state.clear()


@player_router.message(StateFilter(NewPlayer.photo))
async def wrong_photo(message: Message):
    await message.answer(text=NEW_PLAYER['wrong_photo'])
