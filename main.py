import requests
import telebot
import json

TOKEN = "6179594384:AAGCD_4gEv4wgm9TXPdFc-InFQA13e9q_Kg"
bot = telebot.TeleBot(TOKEN)

keys = {
    'евро': 'EUR',
    'доллар': 'USD',
    'фунт': 'GBR',
    'биткоин': 'BTC'
}

@bot.message_handler(commands=['start', 'help'])
def start_exchange(message: telebot.types.Message):
    bot.reply_to(message, f"{message.chat.username},введите команду:\n<с какой валюты>\n<в какую валюту>\n<сумму>\n Список валют /values")

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types = ['text', ])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split()
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена {amount} {quote} к {base} -{total_base}'
    bot.send_message(message.chat.id, text)




bot.polling()
