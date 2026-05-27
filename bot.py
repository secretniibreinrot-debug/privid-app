import telebot
from telebot import types

# Твій робочий токен
bot = telebot.TeleBot("8803136202:AAGQkKSMzLcExYMHUl-fpQ1GWNzQudO2VU8")

@bot.message_handler(commands=['start'])
def start_command(message):
    # Створюємо інлайн-маркап (кнопка під повідомленням)
    markup = types.InlineKeyboardMarkup()
    
    # Створюємо кнопку типу Web App (сайт відкриється прямо всередині Telegram)
    # ЗАМІНИ "https://secretniibreinrot-debug.github.io/privid-app/" 
    web_app_info = types.WebAppInfo(url="https://yourusername.github.io/your-repository/")
    btn_site = types.InlineKeyboardButton(text="👻 Відкрити ПРИВІД", web_app=web_app_info)
    
    # Додаємо кнопку в розмітку
    markup.add(btn_site)
    
    # Текст привітання
    welcome_text = "Привіт! Це мережа ПРИВІД. Твій надійний термінал розіграшів."
    
    # Надсилаємо повідомлення з кнопкою
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# Запуск бота
bot.polling(none_stop=True)