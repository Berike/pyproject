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
        elif message.text == 'Играть!':
            bot.send_message(message.from_user.id, 'too work in progress?');
        # WHICH TYPE
        if message.text == 'Растение':
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        item4 = types.KeyboardButton("большие")
                        item5 = types.KeyboardButton("маленькие")
                        item6 = types.KeyboardButton("нет(")
                        markup.add(item4, item5, item6)
                        bot.send_message(message.chat.id, 'какие цветочки(размер)?', reply_markup=markup)
        if message.text == 'Кустарник':
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        item4 = types.KeyboardButton("большие")
                        item5 = types.KeyboardButton("маленькие")
                        item6 = types.KeyboardButton("нет(")
                        markup.add(item4, item5, item6)
                        bot.send_message(message.chat.id, 'какие цветочки(размер)?', reply_markup=markup)
        # FLOWER SIZE
        if message.text == 'большие':
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                item4 = types.KeyboardButton("желтые")
                                item5 = types.KeyboardButton("белые")
                                item6 = types.KeyboardButton("синие")
                                markup.add(item4, item5, item6)
                                bot.send_message(message.chat.id, 'какие цветочки(цвет)?', reply_markup=markup)
        if message.text == 'маленькие':
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                item4 = types.KeyboardButton("желтые")
                                item5 = types.KeyboardButton("белые")
                                item6 = types.KeyboardButton("синие")
                                markup.add(item4, item5, item6)
                                bot.send_message(message.chat.id, 'какие цветочки(цвет)?', reply_markup=markup)

        # FOR NO FLOWERS?????
        #FLOWERS COLOUR
        if message.text == 'желтые':
            bot.send_message(message.chat.id, 'мхм');
        if message.text == 'белые':
            bot.send_message(message.chat.id, 'ммгуг');
        if message.text == 'синие':
            bot.send_message(message.chat.id, 'амммхм');
        #ЗАПОМНИТЬ ЦВЕТ
        if message.text == 'Дерево':
                        bot.send_message(message.chat.id, 'one sec')




        #elif message.text == 'Играть!':
           # bot.send_message(message.from_user.id, 'too work in progress?');

bot.polling(none_stop=True)
