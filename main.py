import telebot, types
import requests
import json
from telebot import types
import sqlite3
from currency_converter import CurrencyConverter

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
# currency = CurrencyConverter()
# amount = 0
# bot = telebot.TeleBot('5990529068:AAHSDaOozhfSVo5YrGHRqxAKBvI1OkXJX3Q')
# API = '##'

bot = Bot('5990529068:AAHSDaOozhfSVo5YrGHRqxAKBvI1OkXJX3Q')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://www.google.ru/')))
    await message.answer('Hi', reply_markup=markup)

executor.start_polling(dp)

# ВАЛЮТА БОТ
# @bot.message_handler(commands=['start'])
# def message_start(message):
#     bot.send_message(message.chat.id, 'Укажите только сумму')
#     bot.register_next_step_handler(message, summ)
#
#
# def summ(message):
#     global amount
#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         bot.send_message(message.chat.id, 'Ошибка, введите число')
#         bot.register_next_step_handler(message, summ)
#         return
#     if amount > 0:
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='USD/EUR')
#         btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='EUR/USD')
#         btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='USD/GBP')
#         btn4 = types.InlineKeyboardButton('Своя пара', callback_data='else')
#         markup.add(btn1, btn2, btn3, btn4)
#         bot.send_message(message.chat.id, 'Выберете пару валют', reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, 'Ошибка, ведите сумму больше 0')
#         bot.register_next_step_handler(message, summ)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data != 'else':
#         values = call.data.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(call.message.chat.id, f'Получается {round(res, 2)}')
#     else:
#         bot.send_message(call.message.chat.id, 'Введите валютную пару')
#         bot.register_next_step_handler(call.message, my_currency)
#
#
# def my_currency(message):
#     try:
#         values = message.text.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(message.chat.id, f'Получается {round(res, 2)}')
#     except Exception:
#         bot.send_message(message.chat.id, 'Ошибка, проверьте пару')
#         bot.register_next_step_handler(message, my_currency)


# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Укажите город:')
#
#
# @bot.message_handler(content_types=['text'])
# def get_weather(message):
#     city = message.text.strip().lower()
#     res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
#     data = json.loads(res.text)
#     bot.reply_to(message, f'Сейчас температура: {data["main"]["temp"]}')


# name = ''
# @bot.message_handler(commands=['start'])
# def message_start(message):
#     conn = sqlite3.connect('start.sql')  # старт БД, храниться вся БД
#     cur = conn.cursor()  # с помощью него можно управлять БД
#     cur.execute(
#         'CREATE TABLE IF NOT EXISTS user (id int auto_increment primary key, name varchar(50), password varchar(50))'
#     )
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Привет, дальше регистрация')
#     bot.register_next_step_handler(message, user_name)
#
#
# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Теперь придумай пароль)))')
#     bot.register_next_step_handler(message, user_password)
#
#
# def user_password(message):
#     password = message.text.strip()
#
#     conn = sqlite3.connect('start.sql')  # старт БД, храниться вся БД
#     cur = conn.cursor()  # с помощью него можно управлять БД
#     cur.execute(
#         'INSERT INTO user (name, password) VALUES ("%s", "%s")' % (name, password)
#     )
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardMarkup('Список пользователей '))
#     bot.send_message(message.chat.id, 'Вы зареганы')


# @bot.message_handler(commands=['help'])
# def message_help(message):
#     bot.send_message(message.chat.id, 'Это бот')
#
#
# @bot.message_handler()
# def message_text(message):
#     bot.send_message(message.chat.id, 'Я ограниченный бот\n'
#                                       'инфо /help')
#
#
# bot.polling(none_stop=True)
