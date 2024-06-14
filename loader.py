import os

from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

CHANNELS = [{"name": "geeks_test_3", "channel_id": "-1002183977667"}]

ADMIN = os.getenv('ADMIN')
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot, storage=storage)
