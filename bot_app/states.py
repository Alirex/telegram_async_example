from aiogram.dispatcher.filters.state import StatesGroup, State


class ExampleForm(StatesGroup):
    name = State()
    age = State()
    city = State()
