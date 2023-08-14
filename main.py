import telebot, types
import requests
import json
from telebot import types
import sqlite3

bot = telebot.TeleBot('5990529068:AAHSDaOozhfSVo5YrGHRqxAKBvI1OkXJX3Q')
API = '##'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Укажите город:')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    bot.reply_to(message, f'Сейчас температура: {data["main"]["temp"]}')



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


@bot.message_handler(commands=['help'])
def message_help(message):
    bot.send_message(message.chat.id, 'Это бот')


# @bot.message_handler()
# def message_text(message):
#     bot.send_message(message.chat.id, 'Я ограниченный бот\n'
#                                       'инфо /help')


bot.polling(none_stop=True)
