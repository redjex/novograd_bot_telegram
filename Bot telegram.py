import telebot
from telebot import types

token='Token'
bot=telebot.TeleBot(token)

Answers = "Мой разработчик не говорил что мне делать в таких ситуациях"


@bot.message_handler(commands=['start'])
def start_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Мерия👨‍⚖️")
    item2 = types.KeyboardButton("Воспитаники🏄‍♂️")
    markup.add(item1, item2)
    bot.send_message(message.chat.id,'Привет, теперь выбери свое положение в лагере.\n Мерия👨‍⚖️ \n Воспитаники🏄‍♂️', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Мерия👨‍⚖️":
        bot.send_message(message.chat.id,"Круто что ты у нас!")
    elif message.text == "Воспитаники🏄‍♂️":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Курсы валют📈")
        item2 = types.KeyboardButton("Важная информация💣")
        item3 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3)
        bot.send_message(message.chat.id, "Теперь выбери раздел📑", reply_markup=markup)
    elif message.text == "Назад🔙":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Мерия👨‍⚖️")
        item2 = types.KeyboardButton("Воспитаники🏄‍♂️")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Успешно✅", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, Answers)


if __name__ == '__main__':
    bot.infinity_polling()
