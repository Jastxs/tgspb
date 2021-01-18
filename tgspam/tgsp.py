import telebot

bot = telebot.TeleBot("1584514253:AAFFZrYWU4wElEX0Y26qESDjAoUgy1UzrgM")
#команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'команда: /test' )
@bot.message_handler(content_types=['text'])
def send_text(message):
    #команда /spam
    if message.text.lower() == "/test":
        while True:
            bot.send_message(message.chat.id, 'boku no pico - top  anime')


bot.polling()