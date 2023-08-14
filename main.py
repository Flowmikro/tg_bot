import telebot , types
from telebot import types
import sqlite3

bot = telebot.TeleBot('5990529068:AAHSDaOozhfSVo5YrGHRqxAKBvI1OkXJX3Q')


@bot.message_handler(commands=['start'])
def message_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('/start')
    btn3 = types.KeyboardButton('help')
    markup.row(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)


@bot.message_handler(commands=['help'])
def message_help(message):
    bot.send_message(message.chat.id, 'Это бот')


@bot.message_handler()
def message_text(message):
    bot.send_message(message.chat.id, 'Я ограниченный бот\n'
                                      'инфо /help')


bot.polling(none_stop=True)
