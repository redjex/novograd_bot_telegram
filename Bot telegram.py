#  //=====\\ ||======  ||===== ||=====\\
# //         ||        ||      ||      ||
# ||         ||=====\\ ||===== ||=====//
# \\         ||     || ||      ||
#  \\=====// ||=====// ||===== ||


#  //=====\\ ||\\    //|| ||\\    //||
# //         || \\  // || || \\  // ||
# ||         ||  \\//  || ||  \\//  ||
# \\         ||        || ||        ||
#  \\=====// ||        || ||        ||


import telebot
from telebot import types
import random


# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot_token = '6843771352:AAG7zXjfRK68nlnQbs89D_2Xx13EBqbd_Vk'
bot = telebot.TeleBot(bot_token)


Answers = ["Мой разработчик не говорил что мне делать в таких ситуациях", "Я не знаю ответа", "Буду тактически молчать..", "Думаешь я знаю что это?"]

Test = 0

Damate = 9
Sber = 3
Space_pi = 10
MedIng = 6
MIFI = 11
GEO = 7

path_list = ['2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.jpg' , '10.jpg', '11.jpg', '12.jpg']


@bot.message_handler(commands=['start'])
def send_photo_or_sticker(message):
    print("Бот запущен")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Попробовать🟥")
    markup.add(item1)
    photo_path = '5310089791892741162.jpg'  # Укажите путь к вашей фотографии
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "Привет Новоградец, {0.first_name}!".format(message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, "Отвлекись от всех мыслей и посети каждый раздел бота Новограда :)")


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Попробовать🟥":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Курсы валют📈")
        item2 = types.KeyboardButton("Мемная😂")
        item3 = types.KeyboardButton("Учебка📑")
        item4 = types.KeyboardButton("Тест на знание Новограда")
        item5 = types.KeyboardButton("Код📑")
        item7 = types.KeyboardButton("О Новограде")
        item8 = types.KeyboardButton("Пожертвование💸")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5, item7)
        markup.add(item8)
        bot.send_message(message.chat.id, "Теперь выбери раздел📑", reply_markup=markup)
    elif message.text == "Назад🔙":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Курсы валют📈")
        item2 = types.KeyboardButton("Мемная😂")
        item3 = types.KeyboardButton("Учебка📑")
        item4 = types.KeyboardButton("Тест на знание Новограда")
        item5 = types.KeyboardButton("Код📑")
        item7 = types.KeyboardButton("О Новограде")
        item8 = types.KeyboardButton("Пожертвование💸")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5, item7)
        markup.add(item8)
        bot.send_message(message.chat.id, "Ты заходи если что😉", reply_markup=markup)

    elif message.text == "О Новограде":
        photo_path = '5310089791892741146.jpg'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "https://telegra.ph/Memy-Novograda-2024-08-10-2")
    elif message.text == "Пожертвование💸":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Назад🔙")
        markup.add(item1)
        bot.send_message(message.chat.id, "Солнышко, если ты правда хочешь отправить мне денюшку то\n\nНапиши банкиру что ты готов предать пожертвование\nНа номер 131. За ранее спасибо. \n\nhttps://t.me/:@Nata_Polunovskaya",reply_markup=markup)
    elif message.text == "Учебка📑":
        photo_path = '5310089791892741150.jpg'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Психоподдержка👌")
        item2 = types.KeyboardButton("Описание кейсов🏄‍♂️")
        item3 = types.KeyboardButton("Архив")
        markup.add(item1, item2)
        markup.add(item3)
        bot.send_message(message.chat.id, "Выбери раздел:", reply_markup=markup)
    elif message.text == "Архив":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Фото")
        item2 = types.KeyboardButton("Новоград ТВ")
        item3 = types.KeyboardButton("Гимн Новограда")
        item4 = types.KeyboardButton("Стикеры")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Выбери раздел:", reply_markup=markup)
    elif message.text == "Психоподдержка👌":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("Назад🔙")
        markup.add(item3)
        bot.send_message(message.chat.id, "Мастерская психология подготовила четыре материала, которые могут быть вам полезны в повседневной жизни. Приятного чтения!\n\n 1. Как преодолеть тревожность: https://telegra.ph/Kak-preodolet-trevozhnost-08-09 \n\n2. Как влиться в новый коллектив: https://telegra.ph/Kak-vlitsya-v-novyj-kollektiv-08-09 \n\n3. Как бороться с самокритичными мыслями: https://telegra.ph/Kak-borotsya-s-samokritichnymi-myslyami-08-09 \n\n4. Как определить, что в семье происходит насилие: https://telegra.ph/Kak-opredelit-chto-v-seme-proishodit-nasilie-08-09", reply_markup=markup)

    elif message.text == "Стикеры":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("Назад🔙")
        markup.add(item3)
        bot.send_message(message.chat.id, "Мастерская стикеров сделала крутой пак! Скорее добавляй его себе:", reply_markup=markup)
        bot.send_message(message.chat.id, "https://t.me/addstickers/Novograd2024")
    elif message.text == "Описание кейсов🏄‍♂️":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Дамате🟠")
        item2 = types.KeyboardButton("Сбер✔")
        item3 = types.KeyboardButton("Space Pi🟦")
        item4 = types.KeyboardButton("МедИнж🔺")
        item5 = types.KeyboardButton("МИФИ🔷")
        item6 = types.KeyboardButton("Геоскан🟡")
        item7 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5, item6)
        markup.add(item7)
        bot.send_message(message.chat.id, "📈", reply_markup=markup)
    elif message.text == "Фото":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item7 = types.KeyboardButton("Назад🔙")
        markup.add(item7)
        bot.send_message(message.chat.id, "Фото из Новограда-2024 по дням вы можете найти в этих альбомах:", reply_markup=markup)
        bot.send_message(message.chat.id, "День 1: https://vk.com/album-55502126_305226288\n\nДень 2: https://vk.com/album-55502126_305235708\n\nДень 3: https://vk.com/album-55502126_305244418\n\nДень 4: https://vk.com/album-55502126_305256389\n\nДень 5: https://vk.com/album-55502126_305265959\n\nДень 6: https://vk.com/album-55502126_305291288\n\nДень 7: https://vk.com/album-55502126_305297171\n\nДень 8: https://vk.com/album-55502126_305310909\n\nДень 9: https://vk.com/album-55502126_305315645\n\nДень 10: https://vk.com/album-55502126_305315646")

    elif message.text == "Новоград ТВ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item7 = types.KeyboardButton("Назад🔙")
        markup.add(item7)
        bot.send_message(message.chat.id, "Все выпуски нашей любимой новостной передачи в этом плейлисте:")
        bot.send_message(message.chat.id, "https://vk.com/video/@novograd2024/playlists?z=video-55502126_456239170%2Fclub55502126%2Fpl_-55502126_54058391", reply_markup=markup)
    # Кейсы
    elif message.text == "Гимн Новограда":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item7 = types.KeyboardButton("Назад🔙")
        markup.add(item7)
        bot.send_message(message.chat.id, "Опа, а вот и ваш любимый гимн", reply_markup=markup)
        bot.send_message(message.chat.id, "https://drive.google.com/file/d/1L5955yw8Gg92IK1COfHLeIW9w1XI2IIW/view?usp=drive_link")
        print("Nice")


    elif message.text == "Дамате🟠":
        bot.send_message(message.chat.id, "Дамате:")
        bot.send_message(message.chat.id, "Сельскохозяйственный холдинг «Дамате» является крупнейшим в России и Европе производителем мяса индейки. Сохранить своё лидерство ему помогают инновации и оптимизация текущих технологических процессов, в том числе и способа уборки мусора в птичьих вольерах. Вам предстоит придумать как сделать этот процесс более эффективным и безопасным для обитателей ферм.")
        photo_path = 'novograd_2024_case-damate.pdf'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_document(message.chat.id, photo)
    elif message.text == "Сбер✔":
        bot.send_message(message.chat.id, "Сбер:")
        bot.send_message(message.chat.id,"Команда AI for Social Good от Сбербанка предлагает вам позаботиться о биоразнообразии планеты, используя ИИ. Стажёрам нужно было спроектировать систему машинного обучения для идентификации снежных барсов: больших кошек, которых на всей Земле осталось менее 100 особей.")
        photo_path = 'novograd_2024_case-sberbank (3).pdf'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_document(message.chat.id, photo)
    elif message.text == "Space Pi🟦":
        bot.send_message(message.chat.id, "Space Pi:")
        bot.send_message(message.chat.id, "Научно-образовательный проект Space-π предлагает прикоснуться к космическим технологиям. Вам предстоит разработать бюджетный вариант наземной станции приёма метеорологических данных с космических аппаратов, которую образовательные организации по всей стране смогут приобрести для изучения космоса.")
        photo_path = 'novograd_2024_case-spacepi (1).pdf'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_document(message.chat.id, photo)
    elif message.text == "МедИнж🔺":
        bot.send_message(message.chat.id, "МедИнж:")
        bot.send_message(message.chat.id,"МедИнж — крупнейший российский производитель высокотехнологичных имплантируемых медицинских изделий из города Пенза. Вам предстоит подумать над актуальной задачей в области трансплантологии, а именно как снизить до 0 пропускаемость стенок искусственных сосудов.")
        photo_path = 'novograd_2024_case-medeng.pdf'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_document(message.chat.id, photo)
    elif message.text == "МИФИ🔷":
        bot.send_message(message.chat.id, "МИФИ:")
        bot.send_message(message.chat.id,"Национальный исследовательский ядерный университет «МИФИ» и учёные из лаборатории 2D-материалов в электронике, спинтронике и фотонике приглашают вас в будущее микроэлектроники, которое будет не кремниевым, а, скорее всего, углеродным. Углерод имеет множество плюсов, но для микроэлектроники подойдут только его аллотропные формы. Какие именно? Как их получить? Ответить на эти вопросы предстоит именно стажёрам.")
        photo_path = 'novograd_2024_case-mefi.pdf'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_document(message.chat.id, photo)
    elif message.text == "Геоскан🟡":
        bot.send_message(message.chat.id, "Геоскан:")
        bot.send_message(message.chat.id,"Геоскан — российская группа компаний, занимающаяся разработкой и производством беспилотников, малых космических аппаратов и т.п.. Решая кейс вам предстоит подключиться к реализации одного из проектов и предложить свою концепцию БПЛА, предназначенного для осмотра и видеофиксации состояния стенок подземных месторождений полезных ископаемых.")
        photo_path = 'novograd_2024_case-geoscan.pdf'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_document(message.chat.id, photo)




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
        bot.send_message(message.chat.id, "Хоп, а вот и акции компании📈", reply_markup=markup)
    elif message.text == "Получить что? Ничего":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Назад🔙")
        markup.add(item1)
        bot.send_message(message.chat.id, "Потому что Новокотиков у компании нет, лучше нам переведите мне. \n\nId карты 131.", reply_markup=markup)
    elif message.text == "Код📑":
        photo_path = '5310089791892741152.jpg'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Ну-с, давай программируем…\nВот тебе ссылка на GitHub - \nhttps://github.com/redjex/novograd_bot_telegram")
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
    elif message.text == "Мемная😂":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Пояснения😎")
        item3 = types.KeyboardButton("Мемная😂")
        item2 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item3)
        markup.add(item2)
        photo_path = random.choice(path_list)
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Лови мем! \n\nЖми на кнопку «мемная», сколько хочешь. Мемы будут появляться бесконечно (ну почти).", reply_markup=markup)
    elif message.text == "Пояснения😎":
        bot.send_message(message.chat.id, "https://telegra.ph/Memy-Novograda-2024-08-10")
    elif message.text == "Попробовать еще раз🍕":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Москва")
        item2 = types.KeyboardButton("Пенза")
        item3 = types.KeyboardButton("Казань")
        item4 = types.KeyboardButton("Калининград")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        photo_path = 'easy.jpg'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Выбери правильный ответ:\n\nИ узнай как хорошо ты знаешь Новоград или Наноград.",reply_markup=markup)
        bot.send_message(message.chat.id, "В каком городе проходил Новоград-2024?")


    # Изи вопросы


    elif message.text == "Тест на знание Новограда":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Москва")
        item2 = types.KeyboardButton("Пенза")
        item3 = types.KeyboardButton("Казань")
        item4 = types.KeyboardButton("Калининград")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        photo_path = 'easy.jpg'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Выбери правильный ответ:\n\nИ узнай как хорошо ты знаешь Новоград или Наноград.", reply_markup=markup)
        bot.send_message(message.chat.id, "В каком городе проходил Новоград-2024?")
    elif message.text == "Пенза":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("6")
        item2 = types.KeyboardButton("4")
        item3 = types.KeyboardButton("8")
        item4 = types.KeyboardButton("5")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Сколько компаний было в 2024?", reply_markup=markup)
    elif message.text == "6":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Нанокотики")
        item2 = types.KeyboardButton("Новокотики")
        item3 = types.KeyboardButton("Нанорубли")
        item4 = types.KeyboardButton("Рубли")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Как называется валюта Новограда?", reply_markup=markup)
    elif message.text == "Новокотики":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Андрей Тяглый")
        item2 = types.KeyboardButton("Антон Алексеев")
        item3 = types.KeyboardButton("Игорь Семенов")
        item4 = types.KeyboardButton("Влад Рябиков")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Кто мер Новограда в 2024?", reply_markup=markup)
    elif message.text == "Антон Алексеев":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Сбер")
        item2 = types.KeyboardButton("МедИнж")
        item3 = types.KeyboardButton("Геоскан")
        item4 = types.KeyboardButton("Space Pi")
        item5 = types.KeyboardButton("Дамате")
        item6 = types.KeyboardButton("НИЯУ МИФИ")
        item7 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5, item6)
        markup.add(item7)
        bot.send_message(message.chat.id, "Какая компания победила в танцевальном баттле в 2024?", reply_markup=markup)
    elif message.text == "МедИнж":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Павел Гашинов")
        item2 = types.KeyboardButton("Михаил Рядинский")
        item3 = types.KeyboardButton("Владислав Рябиков")
        item4 = types.KeyboardButton("Андрей Тяглый")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Кто в 2024 году занимал пост главы биржи?", reply_markup=markup)
    elif message.text == "Владислав Рябиков":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Тарханы")
        item2 = types.KeyboardButton("Дом Пушкина")
        item3 = types.KeyboardButton("Могила Лермонтова")
        item4 = types.KeyboardButton("Усадьба Льва Толстого")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Какое знаменательное место из истории российской литературы посетили новоградцы?", reply_markup=markup)
    elif message.text == "Тарханы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Олень")
        item2 = types.KeyboardButton("Голубь")
        item3 = types.KeyboardButton("Ласточка")
        item4 = types.KeyboardButton("Медведь")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Какой символ Пензы?", reply_markup=markup)
    elif message.text == "Ласточка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Всё круто")
        item2 = types.KeyboardButton("Ничего")
        item3 = types.KeyboardButton("Спасибо за него")
        item4 = types.KeyboardButton("Он ещё не прошел")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Как прошёл ваш день, Новоград?", reply_markup=markup)
    elif message.text == "Он ещё не прошел":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Владислав Цой")
        item2 = types.KeyboardButton("Андрей Штанюк")
        item3 = types.KeyboardButton("Анастасия Криволапова")
        item4 = types.KeyboardButton("Арсений Соловей")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Кто обычно ведёт вечерние события Новограда?", reply_markup=markup)
    elif message.text == "Андрей Штанюк":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Продолжить?")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item5, item1)
        bot.send_message(message.chat.id, "Поздравляю тебя!\n От нашей команды, ты прошел 1 этап\n Надеемся что ты отгадаешь все остальные ответы!", reply_markup=markup)


    # Медиум вопросы


    elif message.text == "Продолжить?":
        photo_path = 'mid.jpg'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Хорошо, но этот уровень будет сложнее.")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Мэрия")
        item2 = types.KeyboardButton("Стажеры")
        item3 = types.KeyboardButton("Никто")
        item4 = types.KeyboardButton("Дружба")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Кто победил в волейболе в 2024?", reply_markup=markup)
    elif message.text == "Мэрия":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Сотрудник")
        item2 = types.KeyboardButton("Стажер Мэрии")
        item3 = types.KeyboardButton("Куратор")
        item4 = types.KeyboardButton("Волонтер")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Кто получил первый новокотик за лучший мем?", reply_markup=markup)
    elif message.text == "Волонтер":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Экскурсии")
        item2 = types.KeyboardButton("Работа в компаниях")
        item3 = types.KeyboardButton("Танцевальный баттл")
        item4 = types.KeyboardButton("Матч по лапте")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Что было на шестой день Новограда?", reply_markup=markup)
    elif message.text == "Экскурсии":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Кванториум")
        item2 = types.KeyboardButton("Новоград")
        item3 = types.KeyboardButton("Технопарк")
        item4 = types.KeyboardButton("Санаторий")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Какое здание упомянуто в гимне Новограда-2024? ", reply_markup=markup)
    elif message.text == "Кванториум":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("2012")
        item2 = types.KeyboardButton("2014")
        item3 = types.KeyboardButton("2023")
        item4 = types.KeyboardButton("2024  ")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "В каком году прошел первый в истории Новограда и Нанограда матч по лапте между Мэрией и Стажерами?", reply_markup=markup)
    elif message.text == "2024":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("На экскурсии")
        item2 = types.KeyboardButton("В офисе Сбера")
        item3 = types.KeyboardButton("На открытой дискуссии")
        item4 = types.KeyboardButton("На площади Фейнмана")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Где новоградцам нельзя было снимать?", reply_markup=markup)
    elif message.text == "На экскурсии":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("2011")
        item2 = types.KeyboardButton("2024")
        item3 = types.KeyboardButton("2014")
        item4 = types.KeyboardButton("2010")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "В каком году был пензенский Наноград?", reply_markup=markup)
    elif message.text == "2011":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Продолжим далее?")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1)
        markup.add(item5)
        bot.send_message(message.chat.id, "Отличный результат! Никакой визит эксперта тебе не страшен.\nСейчас предлагаю тебе пройти самый сложный лвл.\n\nИ знай если ты уже тут то ты огромный молодец.", reply_markup=markup)

    # Hard lvl


    elif message.text == "Продолжим далее?":
        photo_path = 'hard.jpg'  # Укажите путь к вашей фотографии
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "История Новограда и Нанограда тебе точно знакома. Но истинный ли ты новокот? Давай проверим, сможешь ли ты пройти самый сложный тест")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Антон Алексеев")
        item2 = types.KeyboardButton("Михаил Эпштейн")
        item3 = types.KeyboardButton("Антатолий Шперх")
        item4 = types.KeyboardButton("Елена Казакова")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Кто был первым мэром Нанограда?", reply_markup=markup)
    elif message.text == "Михаил Эпштейн":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("23")
        item2 = types.KeyboardButton("30")
        item3 = types.KeyboardButton("52")
        item4 = types.KeyboardButton("42")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Сколько всего черных ласточек прилетело в Новоград?", reply_markup=markup)
    elif message.text == "30":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Три Дня Дождя")
        item2 = types.KeyboardButton("Андрей Штанюк")
        item3 = types.KeyboardButton("Владислав Цой")
        item4 = types.KeyboardButton("ИИ")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Кто исполнил гимн Новограда-2024?", reply_markup=markup)
    elif message.text == "ИИ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Грибоедова")
        item2 = types.KeyboardButton("Пушкина")
        item3 = types.KeyboardButton("Лермонтова")
        item4 = types.KeyboardButton("Дюма")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Отсылка на произведние какого автора есть в гимне Новограда-2024?", reply_markup=markup)
    elif message.text == "Грибоедова":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Нейросети")
        item2 = types.KeyboardButton("Квадроберы")
        item3 = types.KeyboardButton("Наука")
        item4 = types.KeyboardButton("Вегетарианство")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Какая тема вызвала наибольший ажиотаж на открытой дискуссии?", reply_markup=markup)
    elif message.text == "Вегетарианство":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Шарикопрокат")
        item2 = types.KeyboardButton("Мячикокатание")
        item3 = types.KeyboardButton("Шайбомёт")
        item4 = types.KeyboardButton("Шаровары")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Как назывался стартап, который лежал в основе бизнес игры «Построй компанию. Продай компанию»", reply_markup=markup)
    elif message.text == "Шарикопрокат":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Дамате")
        item2 = types.KeyboardButton("МедИнж")
        item3 = types.KeyboardButton("Сбер<3")
        item4 = types.KeyboardButton("НИЯУ МИФИ")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Какая компания не вступила в войну мемов Новограда-2024?",reply_markup=markup)
    elif message.text == "НИЯУ МИФИ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Получить что? Ничего")
        item5 = types.KeyboardButton("Назад🔙")
        markup.add(item1)
        markup.add(item5)
        bot.send_message(message.chat.id, "Всё верно — ты можешь гордиться званием Истинного Новокота!",reply_markup=markup)
    else:


        # Easy lvl


        if message.text == "Москва":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1
            item1 = types.KeyboardButton("Пояснение😎")
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item1,item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Калининград":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.1
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Казань":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.2
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "4":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.3
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "8":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.4
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "5":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.5
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Нанокотики":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.6
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Нанокоины":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.7
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Рубли":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.8
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Андрей Тяглый":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.9
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Игорь Семенов":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.91
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Влад Рябинов":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.92
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Дом Пушкина":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.93
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Могила Лермонтова":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.94
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Усадьба Льва Толстого":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.95
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Олень":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.96
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Медведь":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.97
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Голубь":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.98
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Все круто":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Спасибо за него":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.991
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Ничего":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.992
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Владислав Цой":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.993
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Анастасия Криволапова":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.994
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Арсений Соловей":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.995
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Никто":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.996
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Стажеры":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.997
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Дружба":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.998
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Не проводился":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1.999
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)

        # Medium lvl


        elif message.text == "Сотрудник":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.1
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Стажер Мэрии":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.2
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Куратор":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.3
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Работа в компаниях":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.4
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Матч по лапте":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.5
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Танцевальный баттл":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.6
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Новоград":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.7
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Технопарк":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.8
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Санаторий":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.9
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "2023":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)# 2.91
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "2011":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)# 2.92
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "2014":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)# 2.93
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "В офисе Сбера":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.94
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "На открытой дискуссии":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.95
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "На площади Фейнмана":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.96
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "2024":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.97
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "2014":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.98
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "2010":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)

            # Hard lvl

        elif message.text == "Антон Алексеев":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Антатолий Шперх":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Елена Казакова":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "52":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "42":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "23":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Три Дня Дождя":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Владислав Цой":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Андрей Штанюк":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Дюма":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Лермонтова":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Пушкина":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Наука":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Нейросети":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Квадроберы":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Шаровары":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Шайбомёт":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Мячикокатание":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Дамате":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "Сбер<3":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        elif message.text == "МедИнж":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # 2.99
            item3 = types.KeyboardButton("Назад🔙")
            markup.add(item3)
            bot.send_message(message.chat.id, "Попробовать еще раз🍕", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, random.choice(Answers))


if __name__ == '__main__':
    bot.infinity_polling()
