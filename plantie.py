import telebot
import random
from random import sample
from telebot import types
import pandas as pd
import numpy as np
bot = telebot.TeleBot('5348727287:AAGuYtgTjrLiSd6XIywhkRh_RqvWi3m6zlM')

base = pd.read_csv('base.csv')
# head = ['types', 'size', 'colour']
# df = pd.DataFrame(head)
list = []
rez = []
raw_indices = []
@bot.message_handler(commands=["start"])
# beginning
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Определять!")
    item2 = types.KeyboardButton("Играть!")
    markup.add(item1)
    markup.add(item2)

    hell = bot.send_message(message.chat.id, 'Привет, что будем делать?', reply_markup=markup)
    bot.register_next_step_handler(hell, bot_type);


@bot.message_handler(content_types=["text"])
# first fork
def bot_type(message):
    global type
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(text = "Растение")
    item2 = types.KeyboardButton(text = "Дерево")
    item3 = types.KeyboardButton(text = "Кустарник")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    if message.text == 'Определять!':
        type = bot.send_message(message.chat.id, 'Что Вы видите перед собой?', reply_markup=markup)
        bot.register_next_step_handler(type, bot_flow);


    elif message.text == 'Играть!':
        bot.send_message(message.from_user.id, 'too work in progress?');

# WHICH TYPE
@bot.message_handler(content_types=["text"])
def bot_flow(message):
    if message.text == 'Растение':
        list.append(message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item4 = types.KeyboardButton("большие")
        item5 = types.KeyboardButton("маленькие")
        #item6 = types.KeyboardButton("нет(")
        markup.add(item4, item5)
        flow = bot.send_message(message.chat.id, 'какие цветочки(размер)?', reply_markup=markup)
   #     bot.register_next_step_handler(flow, get_flow);

    if message.text == 'Кустарник':
        list.append(message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item4 = types.KeyboardButton("большие")
        item5 = types.KeyboardButton("маленькие")
#        item6 = types.KeyboardButton("нет(")
        markup.add(item4, item5)
        flow = bot.send_message(message.chat.id, 'какие цветочки(размер)?', reply_markup=markup)
    if message.text == 'Дерево':
        list.append(message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item4 = types.KeyboardButton("большие")
        item5 = types.KeyboardButton("маленькие")
        #        item6 = types.KeyboardButton("нет(")
        markup.add(item4, item5)
        flow = bot.send_message(message.chat.id, 'какие цветочки(размер)?', reply_markup=markup)
    bot.register_next_step_handler(flow, bot_pet);


# FLOWER SIZE
def bot_pet(message):
    if message.text == 'большие':
        list.append(message.text)
        a = ', '.join(base.petals.unique())
        pet =bot.send_message(message.chat.id, 'Теперь цвет! В базе доступны такие, выберите один', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, a)

    # ЗАЩИТА ОТ ВРЕДИТЕЛЕЙ
    elif message.text == 'маленькие':
        list.append(message.text)
        a = ', '.join(base.petals.unique())
        pet = bot.send_message(message.chat.id, 'Теперь цвет! В базе доступны такие, выберите один',reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, a)



    bot.register_next_step_handler(pet, bot_petal);
def bot_petal(message):
    petal = bot.send_message(message.chat.id, 'И еще раз',reply_markup=telebot.types.ReplyKeyboardRemove())
    list.append(message.text)
    bot.register_next_step_handler(petal, bot_leaf);


#def bot_leaf(message):
#     for i in range(base.shape[1]):  # iterate over rows
#          row_string = ''
#          for j in range(base.shape[1]):  # iterate over columns
#              value = base.astype(str).at[i, j]  # get cell string value
#              row_string += str(value)
#
#          # print(row_string, end="\t")
#
#          # now we have all the cell of a row contatinated in a single string
#          found_all_strings = True
#          for word_to_search in list:
#              # if not str in row_string:
#              if not word_to_search in row_string:
#                  found_all_strings = False
#
#          if found_all_strings:
#              raw_indices.append(i)
#
#      if raw_indices:
#          end = bot.send_message('da da ura')
#          bot.register_next_step_handler(end, aga);
#      else:
#          end = bot.send_message("No rows found")

       #  bot.register_next_step_handler(end, aga);
def aga(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Да")
    item2 = types.KeyboardButton("Нет")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Еще раз?')
    bot.register_next_step_handler(aga, sbros);
def sbros(message):
    if message.text == 'Да':
        list.clear()
        bot.register_next_step_handler(sbros, start);
    elif message.text == 'Нет':
        pass

bot.polling(none_stop=True)
