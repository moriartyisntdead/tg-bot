from telebot import types

from initBot import bot

@bot.message_handler(content_types=['contact'])
def contactHandler(message):
  if message.contact is not None:
    phoneNumber = message.contact.phone_number
    bot.send_message(message.chat.id, f'Дякую за номер телефону: +{phoneNumber}')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    phoneShopButton = types.KeyboardButton(text='Магазин телефонів')
    exchange = types.KeyboardButton(text='Щось додам')

    markup.add(phoneShopButton, exchange)

    bot.send_message(message.chat.id, 'Оберіть бажану функцію',
                     reply_markup=markup)