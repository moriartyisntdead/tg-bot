import telebot
from telebot import types
from telebot.types import BotCommand

from telegramToken import token
from commands.start import start
from commands.about import about
from utils.utils import returnPhoneInfo

from content import samsung, apple

bot = telebot.TeleBot(token)


def executeBotHandler(func, message):
  func(message, bot)


@bot.message_handler(commands=['start'])
def startHandler(message):
  executeBotHandler(start, message)


@bot.message_handler(commands=['about'])
def aboutHandler(message):
  executeBotHandler(about, message)


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


@bot.message_handler(func=lambda message: True)
def messageHandler(message):
  if message.text == 'Магазин телефонів':
    markup = types.InlineKeyboardMarkup()
    samsungButton = types.InlineKeyboardButton(text='Samsung', callback_data='samsung')
    appleButton = types.InlineKeyboardButton(text='Apple', callback_data='apple')

    markup.add(samsungButton, appleButton)
    bot.send_message(message.chat.id, 'Оберіть виробника телефонів', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def textButtonsHandler(callback):
  if callback.data == 'samsung':
    for phones in samsung.data:
      phoneData = returnPhoneInfo(phones)
      markup = types.InlineKeyboardMarkup()
      orderButton = types.InlineKeyboardButton(text='Замовити', callback_data='order')
      markup.add(orderButton)

      bot.send_photo(callback.message.chat.id, phoneData['image'], caption=phoneData['info'], parse_mode='html',
                     reply_markup=markup)

  elif callback.data == 'apple':
    for phones in apple.data:
      phoneData = returnPhoneInfo(phones)
      markup = types.InlineKeyboardMarkup()
      orderButton = types.InlineKeyboardButton(text='Замовити', callback_data='order')
      markup.add(orderButton)

      bot.send_photo(callback.message.chat.id, phoneData['image'], caption=phoneData['info'], parse_mode='html',
                     reply_markup=markup)

  elif callback.data == 'order':
    bot.send_message(callback.message.chat.id, 'Дякуємо за замовлення!')


bot.set_my_commands([
  BotCommand('start', 'Запустити бота'),
  BotCommand('about', 'Про нас')
])

bot.infinity_polling()
