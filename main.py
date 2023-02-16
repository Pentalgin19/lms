from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.dispatcher.filters import BoundFilter
from random import randint
import time


token = '5894158779:AAHvpwU9jrqdR_liYDeGbtdRsTvzj-XeD9A'
bot = Bot(token=token)
dp = Dispatcher(bot)#, storage=MemoryStorage())

cors = []
@dp.message_handler(commands='start')
async def start(mes: types.Message):
    kb= InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text='Меню', callback_data='menu')
    b2 = InlineKeyboardButton(text='Обратная связь', callback_data='call')
    # b3 = InlineKeyboardButton(text='', callback_data='')
    # b4 = InlineKeyboardButton(text='', callback_data='')
    # b5 = InlineKeyboardButton(text='', callback_data='')
    # b6 = InlineKeyboardButton(text='', callback_data='')
    kb.insert(b1)
    kb.insert(b2)
    await bot.send_message(mes.from_user.id,
                           'Привет! тут чтото должно быыть написано типа приветствия и рассказа про кафе',
                           reply_markup=kb)

@dp.callback_query_handler(text='call')
async def cal(call:
              types.CallbackQuery):
    await call.message.delete()
    kb = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text='Основные блюда', callback_data='hot')
    b2 = InlineKeyboardButton(text='Напитки', callback_data='drinks')
    b3 = InlineKeyboardButton(text='Десерты', callback_data='desert')
    kb.insert(b1)
    kb.insert(b2)
    kb.insert(b3)
    await bot.send_message(call.from_user.id, 'Меню', reply_markup=kb)


@dp.callback_query_handler(text='menu')
async def menu(call: types.CallbackQuery):
    await call.message.delete()
    kb = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text='Основные блюда', callback_data='hot')
    b2 = InlineKeyboardButton(text='Напитки', callback_data='drinks')
    b3 = InlineKeyboardButton(text='Десерты', callback_data='desert')
    kb.insert(b1)
    kb.insert(b2)
    kb.insert(b3)
    await bot.send_message(call.from_user.id, 'Меню', reply_markup=kb)

@dp.callback_query_handler(text='hot')
async def hot(call: types.CallbackQuery):
    await call.message.delete()
    kb = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text='Вареники', callback_data='var')
    b2 = InlineKeyboardButton(text='Омлет', callback_data='oml')
    b3 = InlineKeyboardButton(text='Сэндвичи', callback_data='sand')
    b4 = InlineKeyboardButton(text='Каши', callback_data='cash')
    kb.insert(b1)
    kb.insert(b2)
    kb.insert(b3)
    kb.insert(b4)
    await bot.send_message(call.from_user.id, 'Меню', reply_markup=kb)

@dp.callback_query_handler(text='var')
async def var(call: types.CallbackQuery):
    await call.message.delete()
    kb = InlineKeyboardMarkup(row_width=2)
    kb1 = InlineKeyboardMarkup
    kb2 = InlineKeyboardMarkup
    kb3 = InlineKeyboardMarkup


    b1 = InlineKeyboardButton(text='Картошка', callback_data='k')
    b2 = InlineKeyboardButton(text='Вишня', callback_data='v')
    b3 = InlineKeyboardButton(text='Творог', callback_data='t')
    kb.insert(b1)
    kb.insert(b2)
    kb.insert(b3)
    await bot.send_message(call.from_user.id, 'Выберите начинку', reply_markup=kb)



@dp.callback_query_handler(text='k')
async def k(call: types.CallbackQuery):
    global cors
    cors.append('Вареники с картошкой')
    # print(cors)


@dp.callback_query_handler(text='v')
async def v(call: types.CallbackQuery):
    global cors
    cors.append('Вареники с вишней')
    print(345)
    print(cors)


@dp.callback_query_handler(text='t')
async def t(call: types.CallbackQuery):
    global cors
    cors.append('Вареники с творогом')
    print(cors)












if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)