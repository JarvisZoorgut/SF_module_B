import telebot

TOKEN = "5544590468:AAEpu0fgS7s4SXQMWShGxKJ75yG0LmbFU-I"

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Hi')
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")
    print(message.text)
    pass


# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio', 'voice'])
def handle_docs_audio(message: telebot.types.Message):
    bot.reply_to(message, f'Привет, {message.chat.username}')
    print(message.text)
    pass

@bot.message_handler(content_types=['photo'])
def handle_photo(message: telebot.types.Message):
    bot.reply_to(message, f'Привет, {message.chat.username}, отличная картинка! ))')
    pass

bot.polling(none_stop=True)