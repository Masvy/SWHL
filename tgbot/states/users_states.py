from aiogram.fsm.state import StatesGroup, State


class NewPlayer(StatesGroup):
    full_name = State()
    birthday = State()
    growth = State()
    stick_grip = State()
    photo = State()
