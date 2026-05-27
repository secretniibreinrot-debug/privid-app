import telebot
from telebot import types

# СЮДИ ВСТАВ ТОЙ ТОКЕН, ЯКИЙ СКОПІЮВАВ У BOTFATHER ХВИЛИНУ ТОМУ!
bot = telebot.TeleBot("8803136202:AAGwMqAOggIk-KpeY1xMhDKitQ8bvtMlRgY")

@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.InlineKeyboardMarkup()
    
    # Твоє точне посилання на сайт
    web_app_info = types.WebAppInfo(url="https://secretniibreinrot-debug.github.io/privid-app/")
    btn_site = types.InlineKeyboardButton(text="👻 Відкрити ПРИВІД", web_app=web_app_info)
    
    markup.add(btn_site)
    
    welcome_text = "Привіт! Це мережа ПРИВІД. Твій надійний термінал розіграшів."
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

bot.polling(none_stop=True)
