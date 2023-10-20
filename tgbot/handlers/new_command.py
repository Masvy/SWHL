from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.filters import Command, StateFilter, and_f

from states.users_states import NewCommand
from lexicon.users_lexicon import NEW_COMMAND

command_router: Router = Router()


@command_router.message(Command(commands='new_team'),
                        StateFilter(default_state))
async def start_new_command(message: Message, state: FSMContext):
    await message.answer(text=NEW_COMMAND['name'])
    await state.set_state(NewCommand.name)


@command_router.message(StateFilter(NewCommand.name))
async def save_name(message: Message, state: FSMContext):
    await message.answer(text=NEW_COMMAND['foundation'])
    await state.update_data(name=message.text)
    await state.set_state(NewCommand.foundation)


@command_router.message(StateFilter(NewCommand.foundation))
async def save_foundation(message: Message, state: FSMContext):
    await message.answer(text=NEW_COMMAND['arena'])
    await state.update_data(foundation=message.text)
    await state.set_state(NewCommand.arena)


@command_router.message(StateFilter(NewCommand.arena))
async def save_arena(message: Message, state: FSMContext):
    await message.answer(text=NEW_COMMAND['contact'])
    await state.update_data(arena=message.text)
    await state.set_state(NewCommand.contact)


@command_router.message(StateFilter(NewCommand.contact))
async def save_contact(message: Message, state: FSMContext):
    await message.answer(text=NEW_COMMAND['number'])
    await state.update_data(contact=message.text)
    await state.set_state(NewCommand.number)


@command_router.message(StateFilter(NewCommand.number))
async def save_number(message: Message, state: FSMContext):
    await message.answer(text=NEW_COMMAND['data_saved'])
    await state.update_data(number=message.text)
    await state.clear()
