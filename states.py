from aiogram.dispatcher.filters.state import StatesGroup, State


class actions(StatesGroup):
    find = State()
    choose = State()
    weight = State()
    show = State()
    remove = State()

