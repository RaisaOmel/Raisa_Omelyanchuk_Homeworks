import telebot
from City import City
import requests
import json


bot = telebot.TeleBot('6514567770:AAFaL-L5RmzjVpohCj-YyR3iKz6AaPgMWv8')

cities = [City('Минск', '53.893009', '27.567444','Беларусь'),
          City('Гомель','52.4345','30.9754','Беларусь'),
          City('Гродно','53.669353','23.813131','Беларусь'),
          City('Могилев', '53.908410', '30.345630','Беларусь'),
          City('Витебск','55.1904','30.2049','Беларусь'),
          City('Венеция', '45.434341', '12.338780','Италия'),
          City('Киев', '50.450100', '30.523399','Украина'),
          City('Бирмингем', '52.489471', '-1.898575','Англия'),
          City('Манчестер', '53.483959', '-2.244644','Англия'),
          City('Глазго', '55.860916', '-4.251433','Англия'),
          City('Нью-Йорк', '40.712776', '-74.005974','США'),
          City('Слоним','53.093899','25.319071','Беларусь'),
          City('Владивосток','43.10562','131.87353','Россия'),
          City('Барановичи','53.513222','25.990009','Беларусь'),
          ]

def get_countries():
    s=set()
    for i in cities:
        s.add(i.country)
    return list(s)

def send_cities(message):
    lst=[]
    for i in cities:
        if i.country==message.text:
             lst.append(i.name)

    keyboard=telebot.types.ReplyKeyboardMarkup()
    for i in range(0, len(lst), 2):
        try:
            keyboard.add(lst[i], lst[i + 1])
        except Exception:
            keyboard.add(lst[-1],'⬅')
    if len(lst)%2==0:
        keyboard.add('⬅')

    msg = bot.send_message(message.chat.id, 'Выберите город', reply_markup=keyboard)

def get_time(kol):
    s=str(kol%60).rjust(2,'0')
    m=str((kol//60)%60).rjust(2,'0')
    h=str((kol//3600)%24).rjust(2,'0')
    return f'{h}:{m}:{s}'

@bot.message_handler()
def start(message):
    if message.text == '/start':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)#создается клавиатура
        lst=get_countries()
        for i in range(0,len(lst),2):
            try:
                keyboard.add(lst[i],lst[i+1])
            except Exception:
                keyboard.add(lst[-1])

        msg=bot.send_message(message.chat.id, 'Приветствую в телеграмм боте,'
                                          'где вы сможете найти данные о погоде', reply_markup=keyboard)

        bot.register_next_step_handler(msg,send_cities)#зарегистрировать следующий шаг для обработки
    elif message.text=='⬅':
        bot.delete_message(message.chat.id,message_id= message.id)
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # создается клавиатура
        lst = get_countries()
        for i in range(0, len(lst), 2):
            try:
                keyboard.add(lst[i], lst[i + 1])
            except Exception:
                keyboard.add(lst[-1])

        msg = bot.send_message(message.chat.id, 'Выберите страну', reply_markup=keyboard)
        bot.register_next_step_handler(msg, send_cities)  # зарегистрировать следующий шаг для обработки
    else:
        name = message.text
        c = ''
        for i in cities:
            if i.name == name:
                c = i
                break

        if c == '':
            bot.send_message(message.chat.id, 'Такой команды не существует')
        else:
            url = f'https://api.openweathermap.org/data/2.5/weather?lat={c.lat}&lon={c.lon}&appid=3d13d45416f28b31f5935aa56040e871'
            res = requests.get(url).content
            w = json.loads(res)
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.add(telebot.types.InlineKeyboardButton('Узнать подробнее', callback_data=f'more_{c.name}'))
            temp = round(float(w['main']['temp']) - 272, 1)
            bot.send_message(message.chat.id, f'В городе {c.name} сейчас {temp}°C', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def more_weather(callback):
    if callback.data.startswith('more'):
        name = callback.data.split('_')[1]
        c = ''
        for i in cities:
            if i.name == name:
                c = i
                break
        url=f'https://api.openweathermap.org/data/2.5/weather?lat={c.lat}&lon={c.lon}&appid=3d13d45416f28b31f5935aa56040e871'
        res = requests.get(url).content
        w = json.loads(res)
        temp = round(float(w['main']['temp']) - 272, 1)
        temp_min = round(float(w['main']['temp_min']) - 272, 1)
        temp_max = round(float(w['main']['temp_max']) - 272, 1)
        temp_like = round(float(w['main']['feels_like']) - 272, 1)
        pressing = round(float(w['main']['pressure']) *0.75006375541921, 1)
        speed = round(float(w['wind']['speed'])/0.44704, 1)
        timezone = int(w['timezone'])
        sunrise = (int(w['sys']['sunrise'])+timezone)%86400
        sunset = (int(w['sys']['sunset'])+timezone) % 86400
        bot.edit_message_text(text=f'Температура: {temp}°C\nМинимальная температура'
                                   f'{temp_min}°C\nМаксимальная температура: {temp_max}°C\n'
                                   f'Ощущается как{temp_like}°C\nветер {speed} м/с\n'
                                   f'Давление {pressing} мм рт. ст.\n'
                                   f'восход {get_time(sunrise)}  '
                                   f'заход {get_time(sunset)}', chat_id=callback.message.chat.id,
                              message_id=callback.message.id)



bot.polling()
