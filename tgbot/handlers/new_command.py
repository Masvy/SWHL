from aiogram import Router, types, F
from sqlalchemy.orm import sessionmaker
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.filters import Command, StateFilter, and_f
from aiogram.types import Message, CallbackQuery

from keyboards.inline import commands_kb
from states.users_states import NewCommand
from lexicon.users_lexicon import NEW_COMMAND
from filters.new_commands_filters import IsFaudation
from database.commands import add_user_id_com, add_name_com, add_foundation, \
    add_arena, add_contact, add_phone_number

command_router: Router = Router()


@command_router.callback_query(F.data == 'wrong_1')
@command_router.message(Command(commands='new_team'),
                        StateFilter(default_state))
async def start_new_command(update: types.Update, state: FSMContext):
    if isinstance(update, types.CallbackQuery):
        await update.message.answer(text=NEW_COMMAND['name'])
        await state.set_state(NewCommand.name)
    else:
        await update.answer(text=NEW_COMMAND['name'])
        await state.set_state(NewCommand.name)


@command_router.message(StateFilter(NewCommand.name),
                        lambda x: len(x.text) <= 50)
async def save_name(message: Message, state: FSMContext):
    await message.answer(text=NEW_COMMAND['foundation'])
    await state.update_data(name=message.text)
    await state.set_state(NewCommand.foundation)


@command_router.message(StateFilter(NewCommand.name))
async def wrong_name(message: Message):
    await message.answer(text=NEW_COMMAND['wrong_name'])


@command_router.message(StateFilter(NewCommand.foundation),
                        IsFaudation())
async def save_foundation(message: Message, state: FSMContext):
    await message.answer(text=NEW_COMMAND['arena'])
    await state.update_data(foundation=message.text)
    await state.set_state(NewCommand.arena)


@command_router.message(StateFilter(NewCommand.foundation))
async def wrong_foundation(message: Message):
    await message.answer(text=NEW_COMMAND['wrong_foundation'])


@command_router.message(StateFilter(NewCommand.arena),
                        lambda x: len(x.text) <= 35)
async def save_arena(message: Message, state: FSMContext):
    await message.answer(text=NEW_COMMAND['contact'])
    await state.update_data(arena=message.text)
    await state.set_state(NewCommand.contact)


@command_router.message(StateFilter(NewCommand.arena))
async def wrong_arena(message: Message):
    await message.answer(text=NEW_COMMAND['wrong_arena'])


@command_router.message(StateFilter(NewCommand.contact),
                        and_f(lambda x: x.text.replace(' ', 'a').isalpha(),
                        lambda x: x.text.count(' ') == 1 or
                        x.text.count(' ') == 2, lambda x: len(x.text) <= 50))
async def save_contact(message: Message, state: FSMContext):
    await message.answer(text=NEW_COMMAND['number'])
    await state.update_data(contact=message.text)
    await state.set_state(NewCommand.number)


@command_router.message(StateFilter(NewCommand.contact))
async def wrong_contact(message: Message):
    await message.answer(text=NEW_COMMAND['wrong_contact'])


@command_router.message(StateFilter(NewCommand.number),
                        lambda x: len(x.text) == 11)
async def save_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(text=f'Название команды: {data["name"]}\nГод '
                         f'основания: {data["foundation"]}\nДомашняя '
                         f'арена: {data["arena"]}\nФИО контактного лица: '
                         f'{data["contact"]}\nНомер контактного лица: '
                         f'{data["number"]}\n\nПроверьте, все ли данные '
                         'верны?', reply_markup=commands_kb)


@command_router.message(StateFilter(NewCommand.number))
async def wrong_number(message: Message):
    await message.answer(text=NEW_COMMAND['wrong_number'])


@command_router.callback_query(F.data == 'right_1')
async def save_data_1(callback: CallbackQuery,
                      state: FSMContext,
                      session_maker: sessionmaker):
    data = await state.get_data()
    await add_user_id_com(session_maker, callback.from_user.id)
    await add_name_com(session_maker, callback.from_user.id, data['name'])
    await add_foundation(session_maker, callback.from_user.id,
                         data['foundation'])
    await add_arena(session_maker, callback.from_user.id,
                    data['arena'])
    await add_contact(session_maker, callback.from_user.id, data['contact'])
    await add_phone_number(session_maker, callback.from_user.id,
                           data['number'])
    await callback.message.edit_text(text=NEW_COMMAND['data_saved'])
    await state.clear()
