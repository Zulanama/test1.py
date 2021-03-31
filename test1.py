import telebot
from telebot import types

bot = telebot.TeleBot("1602520785:AAGC6AGQB7WhpZulMnRbzdiUaTDi0zi5-ts") # You can set parse_mode by default. HTML or MARKDOWN
b=int(0)

def main():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('Баллы за тренировку')
    key2 = types.KeyboardButton('Доп за упражнение')
    key3 = types.KeyboardButton('Баланс')
    key4 = types.KeyboardButton('Списать бонусы')
    markup.add(key1, key2, key3, key4)
    return markup
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет. Начислим тебе немного баллов?)', reply_markup=main())

@bot.message_handler(content_types=['text'])
def cont(message):
    global b
    if message.text == 'Баллы за тренировку':
        bot.send_message(message.chat.id, 'Тренировка засчитана', reply_markup=main())
        b+=30
        bot.send_message(message.chat.id, b, reply_markup=main())
    elif message.text == 'Доп за упражнение':
        bot.send_message(message.chat.id, 'Доп баллы начисленны', reply_markup=main())
        b+=5
        bot.send_message(message.chat.id,b, reply_markup=main())
    elif message.text == 'Баланс':
        bot.send_message(message.chat.id, 'Баланс бонусов', reply_markup=main())
        bot.send_message(message.chat.id,b, reply_markup=main())
    elif message.text == 'Списать бонусы':
        bot.send_message(message.chat.id, 'Бонусы списаны. Баланс', reply_markup=main())
        b=0
        bot.send_message(message.chat.id, b, reply_markup=main())
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', reply_markup=main())

bot.polling()
