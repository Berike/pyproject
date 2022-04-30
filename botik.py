import telebot;
from telebot import types;

bot = telebot.TeleBot('5105207162:AAE80aQEgJ_TpF5OfBXfdgOChmfMtUTGagI');

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	but1 = types.KeyboardButton("хочу определить растение")
	but2 = types.KeyboardButton("вторая кнопка")
	markup.add(but1, but2)
	bot.reply_to(message, "Здравствуй".format(message.from_user),parse_mode='html',reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def menu(message):
	if message.text == "хочу определить растение":
		bot.send_message(message.chat.id, 'так...')
		def menu(message):
			but3 = types.KeyboardButton("есть корни")
			but4 = types.KeyboardButton("нет корней")
			markup.add(but3, but4)
			if message.text == "есть корни":
				bot.send_message(message.chat.id, 'Хах, это растение!')
			elif message.text == "нет корней":
				bot.send_message(message.chat.id, 'Это скорее всего не растение...')				
	

	elif message.text == "вторая кнопка":
		bot.send_message(message.chat.id, 'РАЗУМЕЕТСЯ')
	else:
		bot.send_message(message.chat.id, "?")
			

bot.polling(none_stop=True)