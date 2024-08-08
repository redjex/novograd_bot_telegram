import telebot
from telebot import types

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot_token = '6843771352:AAG7zXjfRK68nlnQbs89D_2Xx13EBqbd_Vk'
bot = telebot.TeleBot(bot_token)


Answers = "Мой разработчик не говорил что мне делать в таких ситуациях"

Damate = 9
Sber = 3
Space_pi = 10
MedIng = 5
MIFI = 11
GEO = 7


@bot.message_handler(commands=['start'])
def send_photo_or_sticker(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Попробывать🟥")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Привет, теперь выбери свое положение в лагере.\n Мерия👨‍⚖️ \n Воспитаники🏄‍♂️', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Попробывать🟥":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Курсы валют📈")
        item2 = types.KeyboardButton("Важная информация💣")
        item3 = types.KeyboardButton("Назад🔙")
        item4 = types.KeyboardButton("Код📑")
        markup.add(item1, item2)
        markup.add(item3, item4)
        bot.send_message(message.chat.id, "Теперь выбери раздел📑", reply_markup=markup)
    elif message.text == "Назад🔙":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Попробывать🟥")
        markup.add(item1)
        bot.send_message(message.chat.id, "Успешно✅", reply_markup=markup)
    elif message.text == "Курсы валют📈":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Дамате🟧")
        item2 = types.KeyboardButton("Сбер✅")
        item3 = types.KeyboardButton("Space Pi🔷")
        item4 = types.KeyboardButton("МедИнж🟥")
        item5 = types.KeyboardButton("МИФИ🟦")
        item6 = types.KeyboardButton("Геоскан🟨")
        item7 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5, item6)
        markup.add(item7)
        bot.send_message(message.chat.id, "Вот все курсы валют на данный момент", reply_markup=markup)
    elif message.text == "Код📑":
        bot.send_message(message.chat.id, "Ссылка на GitHub - \nhttps://github.com/redjex/novograd_bot_telegram")
    elif message.text == "Дамате🟧":
        bot.send_message(message.chat.id, f"Damate: {Damate}")
    elif message.text == "Сбер✅":
        bot.send_message(message.chat.id, f"Сбер: {Sber}")
    elif message.text == "Space Pi🔷":
        bot.send_message(message.chat.id, f"Space Pi: {Space_pi}")
    elif message.text == "МедИнж🟥":
        bot.send_message(message.chat.id, f"МедИнж: {MedIng}")
    elif message.text == "МИФИ🟦":
        bot.send_message(message.chat.id, f"МИФИ: {MIFI}")
    elif message.text == "Геоскан🟨":
        bot.send_message(message.chat.id, f"Геоскан: {GEO}")
    elif message.text == "Важная информация💣":
        photo_path = '1.jpg'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Вот твои мемы:")
    else:
        bot.send_message(message.chat.id, Answers)


if __name__ == '__main__':
    bot.infinity_polling()
    
