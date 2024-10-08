'''
tg bot :https://t.me/NurislomsMovi_bot
'''

from telebot import TeleBot
from telebot.types import Message, CallbackQuery

import requests

from buttons import main_button, cities_buttons

bot = TeleBot("8095041126:AAGZfNT67vekJTqFECMjsOZvuf2BG7o9Wr4")



parameters = {
    "appid": "9fcd25b521763c53b9de15f96d26d27a",
    "units": "metric",
}


@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Ob-havo botiga xush kelibsiz!",
                     reply_markup=main_button())

@bot.callback_query_handler(func=lambda call: call.data == 'loc')
def reaction_to_ob_havo(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
    bot.send_message(chat_id, "Locatsiyani yuboring")


@bot.message_handler(content_types=['location'])
def loc(message: Message):
    chat_id = message.chat.id
    long = message.location.longitude
    lat = message.location.latitude
    parameters['lat'] = lat
    parameters['lon'] = long

    data = requests.get("https://api.openweathermap.org/data/2.5/weather?", params=parameters).json()
    temp = data["main"]["temp"]
    wind = data["wind"]["speed"]
    text = f"Ob havo ma'lumoti\nTemp: {temp}C\nWind: {wind}"

    bot.send_message(chat_id, text)


bot.polling()