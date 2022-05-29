import telebot
from telebot import types

# Создаем бота
bot = telebot.TeleBot('5565305975:AAFuGTGP_bo2e4uDYxZ-ENfvXUDzzmfuFFM')
# Команда start
@bot.message_handler(commands=["start"])
def start(message):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("??")
        item2=types.KeyboardButton("Игра!")
        markup.add(item1)
        markup.add(item2)

        bot.send_message('Привет, что будем делать?' ,  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.text == '??' :
            bot.send_message(message.chat.id, 'есть корень?');
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("да")
            item2 = types.KeyboardButton("нет")
            markup.add(item1)
            markup.add(item2)
    if message.text == 'да' :
            bot.send_message(message.chat.id, 'растение!');
    if message.text == 'нет':
            bot.send_message(message.chat.id, ' не растение!');


    elif message.text == 'Игра!':
            bot.send_message(message.from_user.id, 'too work in progress?');
# Запускаем бота
bot.polling(none_stop=True)
