import telebot
from telebot import types


bot = telebot.TeleBot('')

@bot.message_handler(commands=["start"])
# beginning
def start(message):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Определять!")
        item2=types.KeyboardButton("Играть!")
        markup.add(item1)
        markup.add(item2)

        bot.send_message(message.chat.id, 'Привет, что будем делать?',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
# first fork
def bot_message(message):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Растение")
        item2=types.KeyboardButton("Дерево")
        item3 = types.KeyboardButton("Кустарник")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        if message.text == 'Определять!' :
            bot.send_message(message.chat.id, 'Что Вы видите перед собой?',  reply_markup=markup)
        if message.text == 'Растение':
            bot.send_message(message.chat.id, 'растение!');
        if message.text ==  'Кустарник':
            bot.send_message(message.chat.id, 'растение!');
        if message.text == 'Дерево':
            bot.send_message(message.chat.id, ' не растение!');
        elif message.text == 'Играть!':
            bot.send_message(message.from_user.id, 'too work in progress?');

        #elif message.text == 'Играть!':
           # bot.send_message(message.from_user.id, 'too work in progress?');

bot.polling(none_stop=True)