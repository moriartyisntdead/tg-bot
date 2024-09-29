# import sys
# import os

# sys.path.append(os.path.abspath('../src/'))

# from utils.utils import getRootDir

def about(message, bot):
  url = 'https://i.pinimg.com/564x/a0/b9/30/a0b930468b3bb3f187ae6338838e8d49.jpg'

  bot.send_photo(message.chat.id, url, caption='Дуже важлива і цікава інформація про бота')

  # with open(os.path.join(getRootDir(), 'assets/images/hello.jpg'), 'rb') as photo:
  #     bot.send_photo(message.chat.id, photo, caption='Дуже важлива і цікава інформація про бота')
