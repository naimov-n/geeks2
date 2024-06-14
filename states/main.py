from aiogram.dispatcher.filters.state import StatesGroup, State

class MyStates(StatesGroup):
    fio = State()
    phone = State()
    about = State()

class MyAdminStates(StatesGroup):
    message = State()