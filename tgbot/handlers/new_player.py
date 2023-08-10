from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.filters import Command, StateFilter, and_f

from states.users_states import NewPlayer
from lexicon.users_lexicon import NEW_PLAYER
from filters.new_player_filters import IsBirthday


player_router: Router = Router()


@player_router.message(Command(commands='new_player'),
                       StateFilter(default_state))
async def start_new_player(message: Message, state: FSMContext):
    await message.answer(text=NEW_PLAYER['full_name'])
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
async def seve_photo(message: Message, state: FSMContext):
    await message.answer(text=NEW_PLAYER['data_saved'])
    await state.update_data(photo=message.text)
    await state.clear()


@player_router.message(StateFilter(NewPlayer.photo))
async def wrong_photo(message: Message):
    await message.answer(text=NEW_PLAYER['wrong_photo'])