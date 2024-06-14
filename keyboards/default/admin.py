from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def get_start_admin():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(KeyboardButton("/start")).insert(KeyboardButton("/statistika"))
    btn.add(KeyboardButton("/post")).insert(KeyboardButton("/users"))

    return btn