import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('6694175005:AAFk1AhJFHvC04Li8hP5PXuh3tgEaozoLJc')

# Функция для создания клавиатуры с кнопками
def create_keyboard_start():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('Селфи')
    button2 = KeyboardButton('Школьное фото')
    button3 = KeyboardButton('Увлечения')
    keyboard.add(button1, button2, button3)
    return keyboard

def create_keyboard_other():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button4 = KeyboardButton('Про GPT')
    button5 = KeyboardButton('Про разницу между SQL и NoSQL')
    button6 = KeyboardButton('Про первую любовь')
    button7 = KeyboardButton('Предыдущие варианты')
    keyboard.add(button4, button5, button6, button7)
    return keyboard

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
                     "Привет! Этот бот создан как тестовое задание на должность куратора детей по Python Василисой Ковалевой. Давайте с ней познакомимся) \n Есть несколько опций для знакомства: \n Посмотреть последнее селфи \n Посмотреть школьное фото \n Прочесть про увлечения \n Чтобы посмотреть другие варианты взаимодействия, напишите \"/other\"", 
                     reply_markup=create_keyboard_start())

@bot.message_handler(commands=['other'])
def other(message):
    bot.send_message(message.chat.id, 
                     "Что ещё можно посмотреть: \n Послушать объяснения для Бабули про GPT \n Послушать объяснения для Бабули про разницу между SQL и NoSQL \n Послушать историю первой любви", 
                     reply_markup=create_keyboard_other())

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "/other":
        bot.send_message(message.chat.id, 'Остальные варианты', reply_markup=create_keyboard_other())
    elif message.text == 'Про GPT':
        bot.send_message(message.chat.id, "Вы выбрали послушать объяснения для Бабули про GPT")
    elif message.text == 'Про разницу между SQL и NoSQL':
        bot.send_message(message.chat.id, "Вы выбрали послушать объяснения для Бабули про разницу между SQL и NoSQL")
    elif message.text == 'Про первую любовь':
        bot.send_message(message.chat.id, "Вы выбрали послушать про первую любовь Василисы")
    elif message.text == 'Предыдущие варианты':
        bot.send_message(message.chat.id, 
                         "Вы выбрали предыдущие варианты",
                         reply_markup=create_keyboard_start())
    elif message.text == 'Селфи':
        image_url_1 = 'https://sun9-79.userapi.com/impg/bmsbrWA-3K3b8ekiyi0Tiz0UgYGhYzGJ1h44Pg/KJHXu5KSVLM.jpg?size=1620x2160&quality=96&sign=ba35ea6c2ce041c5a5c22efd76a35213&type=album'
        bot.send_photo(message.chat.id, image_url_1, caption="Вы выбрали посмотреть последнее селфи Василисы")
        #bot.send_message(message.chat.id, "Вы выбрали посмотреть последнее селфи Василисы")
    elif message.text == 'Школьное фото':
        image_url_2 = 'https://sun9-69.userapi.com/impf/c9268/v9268350/754/0glEpMt3FCo.jpg?size=1280x851&quality=96&sign=a3fb494c2bca27f471c61201c566c702&type=album'
        bot.send_photo(message.chat.id, image_url_2, caption="Вы выбрали посмотреть школьное фото Василисы")
        #bot.send_message(message.chat.id, "Вы выбрали посмотреть школьное фото Василисы")
    elif message.text == 'Увлечения':
        hobbies = "Меня зовут Василиса, мне 27 лет. Моё главное увлечение - это искусство!" \
                   "Я художник. Я пишу картины и создаю арт-игры \n" \
                   "Я считаю, что игры - это новый медиум в искусстве. \n" \
                   "Они предоставляют огромный спектр инструментов для донесения художественного видения до зрителя.\n" \
                   "Я стараюсь популяризировать арт-игры, участвую в многих арт-резиденциях и работаю с грантами. \n" \
                   "Главной темой моего искусства является Потустороннее и Непознанное - связь нашего Сознания и Подсознания"

        bot.send_message(message.chat.id, "Вы выбрали прочесть про увлечения Василисы: ", hobbies, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "Выберите один из предложенных вариантов или другие варианты, написав \"/other\"", 
                         reply_markup=create_keyboard_start())

# Запуск бота
bot.polling(none_stop=True, interval=0)