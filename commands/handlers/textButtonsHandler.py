import json

from telebot import types

from initBot import bot
from content import samsung, apple
from utils.utils import returnPhoneInfo, getRootDir


@bot.callback_query_handler(func=lambda call: True)
def textButtonsHandler(callback):
  if callback.data == 'samsung':
    orderProduct(samsung.data, callback)
    # for phones in samsung.data:
    #   phoneData = returnPhoneInfo(phones)
    #   markup = types.InlineKeyboardMarkup()
    #   orderButton = types.InlineKeyboardButton(text='Замовити', callback_data='order')
    #   markup.add(orderButton)
    #
    #   bot.send_photo(callback.message.chat.id, phoneData['image'], caption=phoneData['info'], parse_mode='html',
    #                  reply_markup=markup)

  elif callback.data == 'apple':
    orderProduct(apple.data, callback)
    # for phones in apple.data:
    #   phoneData = returnPhoneInfo(phones)
    #   markup = types.InlineKeyboardMarkup()
    #   orderButton = types.InlineKeyboardButton(text='Замовити', callback_data='order')
    #   markup.add(orderButton)
    #
    #   bot.send_photo(callback.message.chat.id, phoneData['image'], caption=phoneData['info'], parse_mode='html',
    #                  reply_markup=markup)

  elif callback.data == 'order':
    bot.send_message(callback.message.chat.id, 'Дякуємо за замовлення!')

def orderProduct(products, callback):
  for product in products:
    phoneData = returnPhoneInfo(product)
    markup = types.InlineKeyboardMarkup()
    orderButton = types.InlineKeyboardButton(text='Замовити', callback_data='order')
    markup.add(orderButton)

    bot.send_photo(callback.message.chat.id, phoneData['image'], caption=phoneData['info'], parse_mode='html',
                   reply_markup=markup)