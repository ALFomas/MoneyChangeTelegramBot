# Итоговое задание 5.6.1 (PJ-02)

import telebot
from extensions import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['voice', ])
def repeat(message: telebot.types.Message):
    """ function to reply to audio messages"""
    bot.send_message(message.chat.id, 'Аудио сообщения зло! \n /help для того что бы понять как работает бот')


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    """function of reply to the sent image"""
    bot.reply_to(message, 'Отличное изображение! \n /help для того что бы понять как работает бот ')


@bot.message_handler(commands=['start', ])
def start(message: telebot.types.Message):
    """ function to display a welcome message"""
    text = f'YO! Приветствую, {message.chat.username} \n ' \
           'В Телеграмм Бот Конвектор Валют\n' \
           '/help для справки \n ' \
           '/values для отображения доступных валют'
    bot.send_message(message.chat.id, text, )


@bot.message_handler(commands=['help', ])
def help(message: telebot.types.Message):
    """ function to display a welcome message"""
    text = 'Этот Телеграмм Бот конвектирует некоторые виды валют \n' \
           'Что бы начать работу введите команду в следующем формате: \n' \
           '<наименование имеющейся валюты> \ <наименование валюты в которую нужно перевести> \ <сумма перевода> \n'

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    """function to display available currency"""
    text = 'Доступные валюты:'
    for i in keys.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    """function to display total price or error message"""
    try:
        values = message.text.split()

        if len(values) != 3:
            raise ConvertionException('Задано слишком много параметров.')

        quote, base, amount = values
        total_price = ManyConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя:\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду:\n {e}')
    else:
        text = f' В {amount} {quote} ---> {total_price} {base} '
        bot.send_message(message.chat.id, text)


bot.polling()
