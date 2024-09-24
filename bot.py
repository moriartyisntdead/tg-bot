import telebot
from tgToken import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello')

@bot.message_handler(commands=['test'])
def test(message):
    bot.reply_to(message, 'Test')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b>', parse_mode='HTML')

# bot.infinity_polling()

bot.polling(none_stop=True)