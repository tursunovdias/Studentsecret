import telebot
from telebot import types

token = '497515988:AAGffsja83LE9js2D1XT-YRNVlfuDoL7Y0w'

bot = telebot.TeleBot(token)

"""
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)
"""

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, '+ message.chat.first_name +'! Чтобы узнать перечень команд, нажмите -------> /help')
  

@bot.message_handler(commands=["website"])
def handle_website(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на наш сайт", url="almaz-borovoe.kz")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Здравствуйте! Нажмите на кнопку и перейдите на наш официальный сайт!.", reply_markup=keyboard)


@bot.message_handler(commands=["gallery"])
def handle_gallery(message):
      photo1 = open("1.jpg", 'rb')
      bot.send_photo(message.chat.id, photo1, 'Санаторий "Алмаз"')
      photo2 = open("2.jpg", 'rb')
      bot.send_photo(message.chat.id, photo2, 'Детская игровая комната')
      photo3 = open("3.jpg", 'rb')
      bot.send_photo(message.chat.id, photo3, 'Номер класса "Полулюкс"')
      photo4 = open("4.jpg", 'rb')
      bot.send_photo(message.chat.id, photo4, 'бассейн для гостей нашего санатория')
      photo5 = open("5.jpg", 'rb')
      bot.send_photo(message.chat.id, photo5, 'Отпразднуйте "Наурыз" у нас')
      photo6 = open("6.jpg", 'rb')
      bot.send_photo(message.chat.id, photo6, 'Номер класса "Стандарт"')
      photo7 = open("7.jpg", 'rb')
      bot.send_photo(message.chat.id, photo7, 'Дискозал')
      


@bot.message_handler(commands=['info'])
def handle_info(message):
    bot.send_message(message.chat.id, '1)Стандартные - секционного типа из 2-х комнат и коридора, душевая, санузел; в каждой комнате есть балкон, тумбочка, посуда, шифоньер,ЖК телевизор, фен, холодильник,две односпальные кровати. На 1чел. 9 000 тенге\n2)Полулюкс 2ч- ком.2х- местный, современный дизайн, душевая, санузел, 2-х спальная кровать, односпальная кровать,ЖК телевизор, холодильник, фен, имеется балкон. Номер на 2-х чел. 24 000 тенге\n3)Люкс 2х-ком. 2х-местный, стильная мебель, столово-чайный сервис, 2 LCD телевизора, холодильник, DVD,чайник,фен,утюг,кондиционер. Номер на 2х чел. 30 000 тенге\n4)Эконом 2х местный, кровать + диван, LCD телевизор, холодильник. Без удобств (туалет, душ на 1 этаже) На 1 чел. 6 000 тенге')

@bot.message_handler(commands=['address'])
def handle_address(message):
    bot.send_message(message.chat.id, ' Наш адрес: Акмолинская область, г. Щучинск. Санаторий «Алмаз». \nТел./факс: 8 (716-36) 9-02-25, \n8 (716-36) 9-03-10.\nсот. \n+7-701-599-46-37, \n+7-701-533-06-05. \n E-mail: rus-brinsh@mail.ru')
   
@bot.message_handler(commands=["instagram"])
def handle_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="instagram", url="https://www.instagram.com/almaz.borovoe/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "follow us in instagram", reply_markup=keyboard)

@bot.message_handler(commands=["entertainment"])
def handle_entertainment(message):
   bot.send_message(message.chat.id, 'Находясь у нас в санатории, вы можете воспользоваться нашими развлечениями, такими как:\n1)бассейн (часы работы:10:00-18:00)\n2)Спортбар(часы работы:21:00-3:00)\n3)бильярдная комната\n4)настольный теннис\n5)кедровая баня на дровах\n6)в зимнее время у нас работает прокат лыж, коньков, санок, снегоходов, так же имеются 2 горки\n7)детская игровая комната\n8)на праздники мы организовываем мероприятия+концертная программа\n9)самый чистый пляж на о.Щучье\n10)множество различных экскурсий!')


@bot.message_handler(commands=['questions'])
def handle_questions(message):
    bot.send_message(message.chat.id, 'Если возникнут вопросы, позвоните +7 (775) 664-97-74')


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, '/info - Прайс лист\n/entertainment - виды досуга и развлечения\n/gallery - фотографии санатория\n/questions - если возникнут вопросы\n/address - контактные данные\n/website - переходите на наш сайт\n/instagram - подписывайтесь на наш инстаграм!')

if __name__ == '__main__':
    bot.polling(none_stop=True)
