from telebot import types
from telebot.types import BotCommand

from initBot import bot
from commands import start, about
# from commands.start import start
# from commands.about import about
from commands.handlers import contactHandler, keyboardButtonsHandler, textButtonsHandler
from utils.utils import returnPhoneInfo


bot.set_my_commands([
  BotCommand('start', 'Запустити бота'),
  BotCommand('about', 'Про нас')
])

bot.infinity_polling()
