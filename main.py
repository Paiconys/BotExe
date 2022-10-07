import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from cfg import TOKEN
import random
import requests
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

inkb = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Рандомное число', callback_data='www'),
                                             InlineKeyboardButton(text='Рандомное число от 1 до 100',
                                                                  callback_data='one_and'),
                                             InlineKeyboardButton(text='Рассписание', callback_data='schedule'),
                                             InlineKeyboardButton(text='Кол-во сообщений всех участников',
                                                                  callback_data='faggot'),
                                             InlineKeyboardButton(text='Button1', callback_data='1'),
                                             InlineKeyboardButton(text='Button2',
                                                                  callback_data='2'),
                                             InlineKeyboardButton(text='Button3', callback_data='3'),
                                             InlineKeyboardButton(text='Button4',
                                                                  callback_data='4'),
                                             InlineKeyboardButton(text='Button5', callback_data='5'),
                                             InlineKeyboardButton(text='Button6',
                                                                  callback_data='6'),
                                             InlineKeyboardButton(text='Button7', callback_data='7'),
                                             InlineKeyboardButton(text='Button8',
                                                                  callback_data='8'))


@dp.message_handler(commands=['start'])
async def command_godota(message: types.Message):
    await bot.send_message(message.chat.id, 'Сасите я бот а вы нет, ахахахахах', reply_markup=inkb)
    while True:
        if message.chat.id != -1001817701706:
            await bot.forward_message(message.chat.id, -1001370851345, message.message_id)
            break
        else:
            await asyncio.sleep(180)
            reg = requests.get("https://api.thecatapi.com/v1/images/search")
            reg = (reg.json())
            reg = (reg[0].get('url'))
            await bot.send_photo(chat_id=message.chat.id, photo=reg)
            await asyncio.sleep(180)
            copypaste = ['рандомный крпипаст 1', 'черный маг', 'рандомный крпипаст 2', 'рандомный крпипаст3',
                         'рандомный крпипаст 4']
            await bot.send_message(chat_id=message.chat.id, text=copypaste[random.randint(0, 4)])


class randomm(StatesGroup):  # 3.3
    one_num = State()
    two_num = State()



@dp.callback_query_handler(text='www')
async def command_godota(callback: types.CallbackQuery):
    await randomm.one_num.set()
    await callback.message.answer('Введите первое число диапозона:')

    @dp.message_handler(state=randomm.one_num)
    async def coin_price_vuvod(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['one_num'] = int(message.text)
        await callback.message.answer(f'Введите второе число диапозона:')
        await randomm.two_num.set()

        @dp.message_handler(state=randomm.two_num)
        async def coin_price_vuvod(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['two_num'] = int(message.text)
            if float(data['two_num']) == float(data['one_num']):
                await randomm.two_num.set()
                await bot.send_message(message.chat.id,
                                       f'Число не должно равняться вашему введенному первому числу({data["one_num"]})\n\nПовторите попытку')
            else:
                await bot.send_message(message.chat.id,
                                       f"Ваша рандомная цифра это: {str(random.randint(data['one_num'], data['two_num']))}\n\nРандом происходил в диапозоне от {data['one_num']} до {data['two_num']}")
                await state.finish()


@dp.callback_query_handler(text='one_and')
async def command_godota(callback: types.CallbackQuery):
    await randomm.one_num.set()
    await callback.message.answer(f'Рандомное число от 1 до 100: {random.randint(1, 100)}')


@dp.message_handler(commands=['godota'])
async def command_godota(message: types.Message):
    await bot.send_poll(chat_id=message.chat.id, question='Go Dota?', options=['yes', 'no'])





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
else:
    print("Dosen't work")