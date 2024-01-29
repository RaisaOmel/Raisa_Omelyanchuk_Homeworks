import telebot
from currency_converter import CurrencyConverter
from telebot import types

amount = 0
bot = telebot.TeleBot('6514567770:AAFaL-L5RmzjVpohCj-YyR3iKz6AaPgMWv8')
currency = CurrencyConverter()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите сумму')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверно. Введите сумму')
        bot.register_next_step_handler(message, summa)
        return
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)  # 2 кнопки в ряду
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('Другое значение', callback_data='else')
        # btn3 = types.InlineKeyboardButton('BYN/EUR', callback_data='byn/eur')
        # btn4 = types.InlineKeyboardButton('EUR/BYN', callback_data='eur/byn')
        # btn5 = types.InlineKeyboardButton('BYN/USD', callback_data='byn/usd')
        # btn6 = types.InlineKeyboardButton('USD/BYN', callback_data='usd/byn')
        #btn7 = types.InlineKeyboardButton('Другое значение', callback_data='else')
        #markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Неверно. Введите сумму больше нуля ')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(callback):
    if callback.data != 'else':
        value = callback.data.upper().split('/')
        rez = currency.convert(amount, value[0], value[1])
        bot.send_message(callback.message.chat.id, f'Результат {round(rez,2)}. Введите сумму')
        bot.register_next_step_handler(callback.message, summa)
    else:
        bot.send_message(callback.message.chat.id, 'Введите пару валют через слэш')
        bot.register_next_step_handler(callback.message, mycurrency)


def mycurrency(message):
    value = message.text.upper().split('/')
    try:
        rez = currency.convert(amount, value[0], value[1])
        bot.send_message(message.chat.id, f'Результат {round(rez,2)}. Введите сумму')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Неверно введены валюты. Введите пару валют через слэш')
        bot.register_next_step_handler(callback.message, mycurrency)


bot.polling(none_stop=True)

