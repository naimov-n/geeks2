from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import CHANNELS, bot


class ChannelMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):

        user = message.from_user
        if user.username:
            ibtn = InlineKeyboardMarkup()
            for channel in CHANNELS:
                user_channel = await bot.get_chat_member(user_id=int(user.id), chat_id=channel.get("channel_id"))
                if user_channel.status == "left":
                    ibtn.add(
                        InlineKeyboardButton(text=channel.get('name'), url=f"https://t.me/{channel.get('name')}"))
                    await message.answer("Iltimos kanalga azo buling:", reply_markup=ibtn)
                    raise CancelHandler()