from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import ADMIN


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if message.from_user.id == int(ADMIN):
            return True
        else:
            return False

