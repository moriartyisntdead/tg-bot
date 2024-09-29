import os
from unittest import skipIf


def getRootDir():
  ROOT_DIR = os.path.abspath(os.curdir)

  return ROOT_DIR


def returnPhoneInfo(phones):
  phoneInfo = (f'{phones['name']} \n'
               f'Технічні характеристики:\n')
  phoneImage = ''
  for idx, phone in enumerate(phones):
    if phone == 'image':
      phoneImage = phones[phone]
    elif phone != 'name' and phone != 'price':
      phoneInfo += f'{phones[phone]} {'/ ' if idx != len(phones) - 3 else ''}'

  phoneInfo += f'\n{phones['price']}'

  return {'image': phoneImage, 'info': phoneInfo}

# def returnGoodsValue(goods):
#   for phones in goods.data:
#     phoneInfo = ''
#     phoneImage = ''
#     for phone in phones:
#       if phone == 'name':
#         phoneInfo += (f'<b>{phones[phone]}</b> \n'
#                       f'Технічні характеристики: ')
#       elif phone == 'image':
#         phoneImage = phones[phone]
#       else:
#         phoneInfo += f' {phones[phone]}'
#
#     return {'image': phoneImage, 'info': phoneInfo}
