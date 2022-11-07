import telebot
from telebot import TeleBot
from telebot import types
from datetime import datetime as dt

TOKEN = "5751311407:AAGx-J_tARNvfRWeIwQ3ZOmojfHKuhoCySw"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton('Калькулятор')
    key2 = types.KeyboardButton('Журнал команд')
    key3 = types.KeyboardButton('Очистить журнал команд')

    kboard.add(key1, key2, key3)

    bot.send_message(message.chat.id, '{0.first_name}, добро пожаловать в калькулятро'.format(
        message.from_user), reply_markup=kboard)


@bot.message_handler(content_types=['text'])
def bot_menu(message):
    time = dt.now().strftime('%H:%M')
    user = message.from_user.first_name
    user_id = str(message.from_user.id)
    text = message.text

    with open('logger.txt', 'a', encoding='UTF-8') as data:
        log_input = ' '.join([time, user, user_id, text])
        data.write(f'{log_input}\n')

    if message.text == 'Калькулятор':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Назад в меню')
        kboard.add(back)

        bot.send_message(message.chat.id, 'Что хотите посчитать? Введите выражение: ',
                         reply_markup=kboard)

    elif message.text == 'Журнал команд':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Назад в меню')
        kboard.add(back)
        bot.send_message(message.chat.id, 'Bot_Log...',
                         reply_markup=kboard)
        with open('logger.txt', 'r', encoding='UTF-8') as db:
            db_out = db.readlines()
            for line in db_out:
                bot.send_message(message.chat.id, {line})

    elif message.text == 'Журнал команд':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        y = types.KeyboardButton('Да')
        n = types.KeyboardButton('Нет')
        kboard.add(y, n)
        bot.send_message(message.chat.id, 'Очистить журнал команд?',
                         reply_markup=kboard)

    elif message.text == 'Нет':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('Калькулятор')
        key2 = types.KeyboardButton('Журнал команд')
        key3 = types.KeyboardButton('Очистить журнал команд')

        kboard.add(key1, key2, key3)

        bot.send_message(message.chat.id, 'Журнал регистрации очищен, возврат в меню',
                         reply_markup=kboard)

    elif message.text == 'Да':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('Калькулятор')
        key2 = types.KeyboardButton('Журнал команд')
        key3 = types.KeyboardButton('Очистить журнал команд')

        kboard.add(key1, key2, key3)

        bot.send_message(message.chat.id, 'Журнал регистрации создан, возврат в меню',
                         reply_markup=kboard)

        log_renew = open('logger.txt', 'w', encoding='UTF-8')
        log_renew.close()

    elif message.text == 'Назад в меню':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('Калькулятор')
        key2 = types.KeyboardButton('Журнал команд')
        key3 = types.KeyboardButton('Очистить журнал команд')

        kboard.add(key1, key2, key3)

        bot.send_message(message.chat.id, '{0.first_name}, добро пожаловать в калькулятро '.format(
            message.from_user), reply_markup=kboard)

    else:
        try:
            value = eval(message.text)
            bot.send_message(message.chat.id, f'{message.text} = {value}')
        except:
            bot.send_message(
                message.chat.id, 'Не могу посчитать такое, попробуй что-то еще: ')


if __name__ == '__main__':
    bot.infinity_polling()