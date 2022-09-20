import telebot
import requests
import json
import extensions

TOKEN = '5544590468:AAEpu0fgS7s4SXQMWShGxKJ75yG0LmbFU-I'

bot = telebot.TeleBot(TOKEN)

class ConvertionException(Exception):
        pass

class CryptoConverter:
        @staticmethod
        def convert(quote: str, base: str, amount: str):
                if quote == base:
                        raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

                try:
                        quote_ticker = keys[quote]
                except KeyError:
                        raise ConvertionException(f'Не удалось обработать валюту {quote}.')

                try:
                        base_ticker = keys[base]
                except KeyError:
                        raise ConvertionException(f'Не удалось обработать валюту {base}.')

                try:
                        amount = float(amount)
                except ValueError:
                        raise ConvertionException(f'Не удалось обработать количество {amount}.')

                url = f"https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"
                payload = {}
                headers = {
                        "apikey": "J2vlt90OZJ5QG6huCpj5k6wHmv1XKYqx"
                }
                r = requests.request("GET", url, headers=headers, data=payload)
                total_base = json.loads(r.content)['result']
                return total_base

keys = {
        'доллар': 'USD',
        'евро': 'EUR',
        'рубль': 'RUB'
}

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
        text = 'Чтобы начать работу, введите команду в следующем формате:\n<имя валюты на русском>\n \
<в какую валюту перевести>\n \
<количество переводимой валюты>\n\nУвидеть список доступных валют:\n /values '
        bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
        text = 'Доступные валюты'
        for key in keys.keys():
                text = '\n'.join((text, key, ))
        bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
        values = message.text.split(' ')
        if len(values) != 3:
                raise ConvertionException('Слишком много параметров')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)

        text = f'Цена {amount} {quote} в {base} = {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()