from telebot import types

from initBot import bot

@bot.message_handler(func=lambda message: True)
def messageHandler(message):
  if message.text == 'Магазин телефонів':
    markup = types.InlineKeyboardMarkup()
    samsungButton = types.InlineKeyboardButton(text='Samsung', callback_data='samsung')
    appleButton = types.InlineKeyboardButton(text='Apple', callback_data='apple')

    markup.add(samsungButton, appleButton)
    bot.send_message(message.chat.id, 'Оберіть виробника телефонів', reply_markup=markup)