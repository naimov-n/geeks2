from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline import get_voice
from keyboards.default import get_start, get_start_admin
from utils.database import users
from states import MyStates
import requests

from loader import bot, dp, ADMIN
like, dislike = 0, 0

@dp.callback_query_handler()
async def callback_query(call: types.CallbackQuery):
    global like, dislike
    data = call.data
    if data == "like":
        like += 1
        await call.answer(f"like {like}")
    elif data == "dislike":
        dislike += 1
        await call.answer(f"dislike {dislike}")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.id == int(ADMIN):
        await message.answer("Assalom aleykum ADMIN!!", reply_markup=await get_start_admin())
    else:
        await message.answer("assalom aleykum botimizga xush kelibsiz!!!", reply_markup=await get_start())
        user = users.get_user_by_id(message.from_user.id)
        if not user:
            users.create_user(message.from_user.id, message.from_user.username)
            await message.answer("F.I.O kiriting: ")
            await MyStates.fio.set()
        elif not len(user[1]) > 0:
            await message.answer("F.I.O kiriting: ")
            await MyStates.fio.set()



@dp.message_handler(state=MyStates.fio)
async def fio(message: types.Message, state: FSMContext):
    print("fio - ", message.text)
    users.update_fio(message.text, message.from_user.id)
    await message.answer("Telefon raqamingizni kiriting:", reply_markup=ReplyKeyboardRemove())
    await MyStates.phone.set()
    # await MyStates.courses.set()

@dp.message_handler(state=MyStates.phone)
async def phone(message: types.Message, state: FSMContext):
    print("phone - ", message.text)
    users.update_phone(message.text, message.from_user.id)
    await message.answer("Uziz haqizda qisqacha malumot kiriting:", reply_markup=ReplyKeyboardRemove())
    await MyStates.about.set()

@dp.message_handler(state=MyStates.about)
async def about(message: types.Message, state: FSMContext):
    print("about - ", message.text)
    users.update_about(message.text, message.from_user.id)
    await message.answer("Qabul qilindi!!!", reply_markup=ReplyKeyboardRemove())
    await state.finish()



@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("nima yordam kerak??", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['sticker'])
async def sticker(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAEMIwFmR3de8u_uvsl-Ivj0wKcEm_sRiwACTQEAAjDUnREwKYXekPr5uDUE")

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact(message: types.Message):
    users.update_user(message.contact.phone_number, message.from_user.id)
    await message.answer("Qabul qilindi!")

@dp.message_handler(commands=['photo'])
async def photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://storage.kun.uz/source/1/aVO4uzANUDBDpwbFJSkKelMuPvDI-RHO.jpg", caption="Sizga yoqdimi??", reply_markup=await get_voice())


@dp.message_handler(commands=['weather'])
async def weather(message: types.Message):
    res = requests.get("http://api.weatherapi.com/v1/current.json?key=637a0367057542d9936143247240705&q=Tashkent")
    if res.status_code == 200:
        response = res.json()
        name = response["location"]["name"]
        country = response["location"]["country"]
        tz = response["location"]["tz_id"]
        temp_c = response["current"]["temp_c"]

        text = (f"<em>Shahar</em> - <b>{name}</b>\n"
                f"<em>Davlat</em> - <b>{country}</b>\n"
                f"<em>Vaqt mintaqasi</em> - <b>{tz}</b>\n"
                f"<em>Xarorat</em> - <b>{temp_c}°C</b>")
        await message.answer(text, parse_mode="HTML")


@dp.message_handler(commands=['currency'])
async def currency(message: types.Message):
    res = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    if res.status_code == 200:
        response = res.json()
        for item in response:
            ccy = item['Ccy']
            name = item['CcyNm_UZ']
            rate = item['Rate']
            if ccy == 'USD' or ccy == 'EUR' or ccy == 'RUB':
                text = (f"<b>{ccy}</b>\n"
                        f"1 {name} - {rate} sum")
                await message.answer(text, parse_mode="HTML")


@dp.message_handler()
async def echo(message: types.Message):
    # await message.answer(message.text)
    # await message.reply(message.text)
    await bot.send_message(chat_id=message.chat.id, text=message.text)




