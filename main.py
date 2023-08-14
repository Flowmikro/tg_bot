import telebot

bot = telebot.TeleBot('5990529068:AAHSDaOozhfSVo5YrGHRqxAKBvI1OkXJX3Q')


@bot.message_handler(commands=['start'])
def message_start(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['help'])
def message_help(message):
    bot.send_message(message.chat.id, 'Это бот')


@bot.message_handler()
def message_text(message):
    bot.send_message(message.chat.id, 'Я ограниченный бот\n'
                                      'инфо /help')


bot.polling(none_stop=True)
