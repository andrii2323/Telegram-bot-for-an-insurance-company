import telebot
from telebot import types

API_TOKEN = "7087398813:AAGgnzS51pFGvPVJFHyxNUo-h5jXdf21LXA"
bot = telebot.TeleBot(API_TOKEN)

# group_chat_id = -1002109787762

previous_menu_markup_dict = {}


# кнопки

# Привітання при виклаці команди "/start"
@bot.message_handler(commands=["start"])
def welcome(message):
    main = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton("Розпочати роботу")
    main.add(start)
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id,
                     f"Ласкаво просимо, {user_name}!\n"
                     " Я Ваш віртуальний страховий помічник!"
                     "Для початку роботи, скористайтеся клавіатурою нижче",
                     reply_markup=main_menu_markup())


# Клавіатура в головному меню
def main_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Страховий випадок")
    button2 = types.KeyboardButton("Калькулятор страхового випадку")
    button3 = types.KeyboardButton("Замовити договір")
    button4 = types.KeyboardButton("Чат з оператором")
    markup.add(button1, button2, button3, button4)
    return markup


# Кнопка для потрапляння в "Головне меню"
@bot.message_handler(func=lambda message: message.text.lower() == "головне меню")
def back_to_main_menu(message):
    bot.send_message(message.chat.id, "Повертаємось до головного меню.", reply_markup=main_menu_markup())


# Кнопки пункта в Головному меню "Страховий випадок"
def insurance_case_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Подорож")
    button2 = types.KeyboardButton("Автомобіль")
    button3 = types.KeyboardButton("Майно")
    button4 = types.KeyboardButton("Здоров'я")
    button5 = types.KeyboardButton("Головне меню")
    markup.add(button1, button2, button3, button4, button5)
    return markup


# Потрапляння в "Страховий випадок"
@bot.message_handler(func=lambda message: message.text.lower() == "страховий випадок")
def insurance_case_menu(message):
    bot.send_message(message.chat.id, "Ви обрали розділ 'Страховий випадок'. Тут ви можете обрати подальші дії.",
                     reply_markup=insurance_case_menu_markup())


# Кнопка "Подорож" в "Страховому випадку"
def trip_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Головне меню")
    button2 = types.KeyboardButton("Назад")
    button3 = types.KeyboardButton("Чат з оператором")
    markup.add(button1, button2, button3)
    return markup


# Потрапляння в кнопку "Подорож"

@bot.message_handler(func=lambda message: message.text.lower() == "подорож")
def trip_info(message):
    previous_menu_markup_dict[message.chat.id] = insurance_case_menu_markup()
    info_message = (
        "Ваші дії:\n"
        "1. Для отримання медичної допомоги за кордоном в першу чергу зверніться за номером телефону, який зазначений у Вашому полісі.\n"
        "2. Будь ласка, надайте оператору наступну інформацію: номер паспорту та договору страхування, адресу перебування і контактні дані для зворотного зв'язку.\n"
        "Якщо Ви самостійно звернулися до лікаря, повідомте нам про це протягом доби з моменту звернення."
    )
    bot.send_message(message.chat.id, info_message, reply_markup=trip_menu_markup())


# Кнопка "Автомобіль" в "Страховому випадку"

def car_insurance_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("КАСКО")
    button2 = types.KeyboardButton("Автоцивілка")
    button3 = types.KeyboardButton("Зелена карта")
    button4 = types.KeyboardButton("Головне меню")
    button5 = types.KeyboardButton("Чат з оператором")
    button6 = types.KeyboardButton("Назад")
    markup.add(button1, button2, button3, button4, button5, button6)
    return markup


# Потрапляння в кнопку "Автомобіль"
@bot.message_handler(func=lambda message: message.text.lower() == "автомобіль")
def car_insurance_menu(message):
    previous_menu_markup_dict[message.chat.id] = insurance_case_menu_markup()
    bot.send_message(message.chat.id, "Ви маєте поліс: ", reply_markup=car_insurance_menu_markup())


# Кнопка "КАСКО" в розділі "Автомобіль"

def kasko_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Назад")
    markup.add(button1)
    return markup


# Потрапляння в "КАСКО" в розділі "Автомобіль"

@bot.message_handler(func=lambda message: message.text.lower() == "каско")
def kasko_info_message(message):
    previous_menu_markup_dict[message.chat.id] = car_insurance_menu_markup()
    info_message = (
        "Ваші дії:\n"
        "1. Протягом 1 (однієї) години, не полишаючи місце події, негайно, сповістити про страховий випадок за телефонами: 0800215553 (безкоштовно на території України) чи +380444902747.\n"
        "2. Викликати Національну поліцію України (НПУ), крім випадків, коли відповідно до умов договору страхування виклик НПУ не є обов'язковим."
    )
    bot.send_message(message.chat.id, info_message, reply_markup=kasko_menu_markup())


# Кнопка "Автоцивілка" в розділі "Автомобіль"
def auto_liability_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Назад")
    markup.add(button1)
    return markup


# Потрапляння в "Автоцивілка" в розділі "Автомобіль"

@bot.message_handler(func=lambda message: message.text.lower() == "автоцивілка")
def auto_liability_info_message(message):
    previous_menu_markup_dict[message.chat.id] = car_insurance_menu_markup()
    info_message = (
        "Ваші дії:\n"
        "1. Протягом 1 (однієї) години не полишаючи місце події, негайно, сповістити про страховий випадок за телефонами: 0800215553 (безкоштовно на території України) чи +380444902747.\n"
        "2.  Викликати Національну поліцію України (НПУ), крім випадків, коли можливе (виконуються умови) оформлення Європротоколу."
    )
    bot.send_message(message.chat.id, info_message, reply_markup=auto_liability_menu_markup())


# Кнопка "Зелена карта" в розділі "Автомобіль"
def green_card_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Назад")
    markup.add(button1)
    return markup


# Потрапляння в "Зелена карта" в розділі "Автомобіль"

@bot.message_handler(func=lambda message: message.text.lower() == "зелена карта")
def green_card_info_message(message):
    previous_menu_markup_dict[message.chat.id] = car_insurance_menu_markup()
    info_message = (
        "Ваші дії:\n"
        "1. Протягом 3 (трьох) робочих днів після повернення в Україну сповістити про страховий випадок за телефонами: +380444902744 чи 0800215553 (безкоштовно на території України).\n"
        "2. Викликати поліцію країни ДТП на місце події, крім випадків, коли можливе оформлення Європротоколу."
    )
    bot.send_message(message.chat.id, info_message, reply_markup=green_card_menu_markup())


# Кнопка "Майно" в розділі "Страховий випадок"
def assets_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Головне меню")
    button2 = types.KeyboardButton("Назад")
    button3 = types.KeyboardButton("Чат з оператором")
    markup.add(button1, button2, button3)
    return markup


# Потрапляння в кнопку "Майно"

@bot.message_handler(func=lambda message: message.text.lower() == "майно")
def assets_info(message):
    previous_menu_markup_dict[message.chat.id] = insurance_case_menu_markup()
    info_message = (
        "Ваші дії:\n"
        "Протягом 2-х діб (без урахування вихідних або святкових днів) з моменту настання страхової події поінформувати про випадок страхову компанію за телефоном 0800215553 (безкоштовно на території України) із зазначенням ПІБ, контактного телефону та № договору страхування (поліса). Повідомте, що саме сталося із застрахованим майном, де воно розташоване, а також дату та час  настання страхового випадку."
    )
    bot.send_message(message.chat.id, info_message, reply_markup=assets_menu_markup())


# Кнопка "Здоров'я" в "Страховий випадок"
def health_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Головне меню")
    button2 = types.KeyboardButton("Запис до лікаря")
    button3 = types.KeyboardButton("Назад")
    markup.add(button1, button2, button3)
    return markup


# Потрапляння в кнопку "Здоров'я"

@bot.message_handler(func=lambda message: message.text.lower() == "здоров'я")
def health_info(message):
    previous_menu_markup_dict[message.chat.id] = insurance_case_menu_markup()
    info_message = (
        "Ваші дії:\n"
        "Для організації медичної допомоги  зверніться, будь ласка,  за номерами,  вказаними у Вашій сервісній  картці. Назвіть № полісу, ПІБ, причину звернення (скарги), Ваше місцезнаходження та контактний номер телефону. Далі дійте  за вказівкою лікаря-координатора страхової компанії."
    )
    bot.send_message(message.chat.id, info_message, reply_markup=health_menu_markup())


# Кнопка "Замовити договір" в розділі "Головне меню"

def order_contract_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton(" Замовити автоцивілку")
    button2 = types.KeyboardButton(" Замовити КАСКО")
    button3 = types.KeyboardButton(" Замовити туристичне страхування")
    button4 = types.KeyboardButton("Замовити страхування майна")
    button5 = types.KeyboardButton("Замовити страхування здоров'я")
    button6 = types.KeyboardButton("Головне меню")
    markup.add(button1, button2, button3, button4, button5, button6)
    return markup


# Потрапляння в кнопку "Замовити договір"

@bot.message_handler(func=lambda message: message.text.lower() == "замовити договір")
def order_contract_menu(message):
    bot.send_message(message.chat.id, "Ви обрали розділ 'Замовити договір'. Тут ви можете обрати подальші дії",
                     reply_markup=order_contract_menu_markup())


# Кнопка "Замовити автоцивілку" в розділі "Замовити договір"
def order_auto_liability():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Чат з оператором")
    button2 = types.KeyboardButton("Назад")
    markup.add(button1, button2)
    return markup


# Потрапляння в кнопку "Замовити автоцивілку"

@bot.message_handler(func=lambda message: message.text.lower() == "замовити автоцивілку")
def order_auto_liability_menu(message):
    previous_menu_markup_dict[message.chat.id] = order_contract_menu_markup()
    info_message = (
        "Ви обрали розділ 'Замовити Автоцивілку'. Для того, щоб замовити автоцивілку, натисніть на кнопку Чат з оператором і напишіть наступні дані:\n"
        "1. ПІБ\n"
        "2. VIN номер автомобіля\n"
        "3. ІПН")
    bot.send_message(message.chat.id, info_message, reply_markup=order_auto_liability())


# Кнопка "Замовити КАСКО" в розділі "Замовити договір"

def order_kasko():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Чат з оператором")
    button2 = types.KeyboardButton("Назад")
    markup.add(button1, button2)
    return markup


# Потрапляння в кнопку "Замовити КАСКО"

@bot.message_handler(func=lambda message: message.text.lower() == "замовити каско")
def order_kasko_menu(message):
    previous_menu_markup_dict[message.chat.id] = order_contract_menu_markup()
    info_message = (
        "Ви обрали розділ 'Замовити КАСКО'. Для того, щоб замовити КАСКО, натисніть на кнопку Чат з оператором і напишіть наступні дані:\n"
        "1. ПІБ\n"
        "2. VIN номер автомобіля\n"
        "3. ІПН")
    bot.send_message(message.chat.id, info_message, reply_markup=order_kasko())


# Кнопка "Замовити туристичне страхування" в розділі "Замовити договір"
def order_tourism():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Чат з оператором")
    button2 = types.KeyboardButton("Назад")
    markup.add(button1, button2)
    return markup


# Потрапляння в кнопку "Замовити туристичне страхування"

@bot.message_handler(func=lambda message: message.text.lower() == "замовити туристичне страхування")
def order_tourism_menu(message):
    previous_menu_markup_dict[message.chat.id] = order_contract_menu_markup()
    info_message = (
        "Ви обрали розділ 'Замовити туристичне страхування'. Для того, щоб замовити туристичне страхування, натисніть на кнопку Чат з оператором і напишіть наступні дані:\n"
        "1. ПІБ\n"
        "2. ІПН\n"
        "3. Серію та номер паспорта")
    bot.send_message(message.chat.id, info_message, reply_markup=order_tourism())


# Кнопка "Замовити страхування майна" в розділі "Замовити договір"
def order_assets():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Чат з оператором")
    button2 = types.KeyboardButton("Назад")
    markup.add(button1, button2)
    return markup


# Потрапляння в кнопку "Замовити страхування майна"
@bot.message_handler(func=lambda message: message.text.lower() == "замовити страхування майна")
def order_assets_menu(message):
    previous_menu_markup_dict[message.chat.id] = order_contract_menu_markup()
    info_message = (
        "Ви обрали розділ 'Замовити туристичне страхування'. Для того, щоб замовити туристичне страхування, натисніть на кнопку Чат з оператором і напишіть наступні дані:\n"
        "1. ПІБ\n"
        "2. ІПН\n"
        "3. Серію та номер паспорта\n"
        "4. Документи на право власності або користуванням майном")
    bot.send_message(message.chat.id, info_message, reply_markup=order_assets())


# Кнопка "Замовити страхування здоров'я" в розділі "Замовити договір"
def order_health():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Чат з оператором")
    button2 = types.KeyboardButton("Назад")
    markup.add(button1, button2)
    return markup


# Потрапляння в кнопку "Замовити страхування здоров'я"
@bot.message_handler(func=lambda message: message.text.lower() == "замовити страхування здоров'я")
def order_health_menu(message):
    previous_menu_markup_dict[message.chat.id] = order_contract_menu_markup()
    info_message = (
        "Ви обрали розділ 'Замовити страхування здоров'я'. Для того, щоб замовити страхування здоров'я, натисніть на кнопку Чат з оператором і напишіть наступні дані:\n"
        "1. ПІБ\n"
        "2. ІПН\n"
        "3. Серію та номер паспорта\n"
        "4. Медичну карту")
    bot.send_message(message.chat.id, info_message, reply_markup=order_health())


# Кнопка "Калькулятор страхового випадку" в розділі "Головне меню"
def insurance_calculator_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Розрахувати страхування здоров'я")
    button2 = types.KeyboardButton("Розрахувати страхування автомобіля")
    button3 = types.KeyboardButton("Розрахувати страхування майна")
    button4 = types.KeyboardButton("Розрахувати страхування подорожі")
    button5 = types.KeyboardButton("Чат з оператором")
    button6 = types.KeyboardButton("Головне меню")
    markup.add(button1, button2, button3, button4, button5, button6)
    return markup


@bot.message_handler(func=lambda message: message.text.lower() == "калькулятор страхового випадку")
def insurance_calculator_menu(message):
    bot.send_message(message.chat.id, "Ви обрали розділ Калькулятор страхового випадку",
                     reply_markup=insurance_calculator_menu_markup())


# Кнопка "Розрахувати вартість здоров'я" в розділі "Калькулятор страхового випадку"
def calculate_health_insurance(message):
    try:
        age = int(message.text)
        insurance_cost = age * 80  # Простий приклад, де вартість страхування залежить від віку
        bot.send_message(message.chat.id, f"Вартість страхування здоров'я: {insurance_cost} грн.")
    except ValueError:
        bot.send_message(message.chat.id, "Будь ласка, введіть числове значення для віку.")


# Потрапляння в кнопку "Розрахувати вартість здоров'я"
@bot.message_handler(func=lambda message: message.text.lower() == "розрахувати страхування здоров'я")
def health_insurance_calculator(message):
    bot.send_message(message.chat.id, "Введіть вік застрахованої особи:")
    bot.register_next_step_handler(message, calculate_health_insurance)


# Кнопка "Розрахувати вартість автомобіля" в розділі "Калькулятор страхового випадку"
def calculate_car_insurance(message):
    try:
        year = int(message.text)
        insurance_cost = (2024 - year) * 130
        bot.send_message(message.chat.id, f"Вартість страхування автомобіля: {insurance_cost} грн")
    except ValueError:
        bot.send_message(message.chat.id, "Будь ласка, введіть числове значення для дати випуску автомобіля.")


# Потрапляння в кнопку "Розрахувати вартість автомобіля"
@bot.message_handler(func=lambda message: message.text.lower() == "розрахувати страхування автомобіля")
def car_insurance_calculator(message):
    bot.send_message(message.chat.id, "Введіть рік випуску автомобіля:")
    bot.register_next_step_handler(message, calculate_car_insurance)


# Кнопка "Розрахувати страхування майна" в розділі "Калькулятор страхового випадку"
def calculate_property_insurance(message):
    try:
        value = int(message.text)
        insurance_cost = value * 2
        bot.send_message(message.chat.id, f"Вартість страхування майна: {insurance_cost} грн")
    except ValueError:
        bot.send_message(message.chat.id, "Будь ласка, введіть числове значення"
                                          " для оціночної вартості майна")


@bot.message_handler(func=lambda message: message.text.lower() == "розрахувати страхування майна")
def property_insurance_calculator(message):
    bot.send_message(message.chat.id, "Введіть оціночну вартість майна:")
    bot.register_next_step_handler(message, calculate_property_insurance)


# Кнопка "Розрахувати вартість подорожі" в розділі "Калькулятор страхового випадку"
def calculate_travel_insurance(message):
    try:
        duration = int(message.text)
        insurance_cost = duration * 150
        bot.send_message(message.chat.id, f"Вартість страхування подорожі: {insurance_cost} грн.")
    except ValueError:
        bot.send_message(message.chat.id, "Будь ласка, введіть числове значення для тривалості подорожі.")


# Потрапляння в кнопку "Розрахувати вартість подорожі"

@bot.message_handler(func=lambda message: message.text.lower() == "розрахувати страхування подорожі")
def travel_insurance_calculator(message):
    bot.send_message(message.chat.id, "Введіть тривалість подорожі (у днях):")
    bot.register_next_step_handler(message, calculate_travel_insurance)


# Логіка кнопки "Назад"
@bot.message_handler(func=lambda message: message.text.lower() == "назад")
def back_to_previous_menu(message):
    if message.chat.id in previous_menu_markup_dict:
        bot.send_message(message.chat.id, "Повертаємось до попереднього меню.",
                         reply_markup=previous_menu_markup_dict[message.chat.id])
    else:
        bot.send_message(message.chat.id, "Попереднє меню не знайдено.")


# Логіка кнопки "Чат з опертаором"

# Словник для зберігання статусу чату з оператором
chat_with_operator = {}

# Словник для зв'язку між повідомленням оператора і ID користувача
operator_to_user = {}

# Ідентифікатор для повідомлення користувача в групу з операторами
group_chat_id = -1002109787762


@bot.message_handler(func=lambda message: message.text.lower() == "чат з оператором")
def start_chat_with_operator(message):
    chat_with_operator[message.chat.id] = True
    bot.send_message(message.chat.id,
                     "Ви увійшли до чату з оператором. Напишіть ваше повідомлення,"
                     " оператор невдовзі приєднається. "
                     "Щоб вийти із чату з оператором напишіть Головне меню")


@bot.message_handler(func=lambda message: message.chat.id in chat_with_operator)
def message_to_operator(message):
    if message.chat.id in chat_with_operator:
        bot.send_message(group_chat_id,
                         f"Повідомлення від {message.from_user.first_name}"
                         f" (ID: {message.from_user.id}): {message.text}")
        operator_to_user[message.from_user.id] = message.chat.id


@bot.message_handler(func=lambda message: message.chat.id == group_chat_id and message.reply_to_message)
def message_from_operator(message):
    user_id = extract_user_id(message.reply_to_message.text)
    if user_id in operator_to_user:
        bot.send_message(operator_to_user[user_id], f"Оператор: {message.text}")


def extract_user_id(text):
    # Текст повідомлення містить ID користувача в дужках, наприклад:
    # "Повідомлення від Ім'я (ID: 123456789)"
    import re
    match = re.search(r'\(ID: (\d+)\)', text)
    return int(match.group(1)) if match else None


if __name__ == '__main__':
    bot.polling(non_stop=True)
