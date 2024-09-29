from telebot import types


def start(message, bot):
  username = message.from_user.username

  if username:
    bot.send_message(message.chat.id, f'Привіт, @{username}!')
  else:
    bot.send_message(message.chat.id, 'Привіт')

  markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
  buttonPhone = types.KeyboardButton(text="Поділитись номером", request_contact=True)

  markup.add(buttonPhone)

  bot.send_message(message.chat.id, 'Для використання бота, будь ласка, поділіться вашим номером телефону',
                   reply_markup=markup)
