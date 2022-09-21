import datetime
import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
        text = 'Чтобы начать работу, введите команду с маленькой буквы в одну строку в следующем формате:\n \
<имя валюты на русском (доллар, евро и т.д.)\n или большими буквами тикеров (USD, EUR и т.д.)>\n \
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
        try:
                values = message.text.split(' ')
                if len(values) != 3 or values == keys['или тикером']:
                        raise ConvertionException('Неверный ввод\n\nПомошь: /help')

                quote, base, amount = values
                total_base = CryptoConverter.convert(quote, base, amount)
        except ConvertionException as e:
                bot.reply_to(message, f'Ошибка пользователя.\n{e}')
        except Exception as e:
                bot.reply_to(message, f'Не удалось обработать команду.\n{e}')
        else:
                dt = (datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                text = f'На {dt}\nЦена {amount} {quote} = {total_base:.2f} {base} '
                bot.send_message(message.chat.id, text)

bot.polling()