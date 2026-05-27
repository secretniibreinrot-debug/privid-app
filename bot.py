import telebot
from telebot import types

# Твій робочий токен
bot = telebot.TeleBot("8803136202:AAGQkKSMzLcExYMHUl-fpQ1GWNzQudo2VU8")

@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.InlineKeyboardMarkup()
    
    # ВИПРАВЛЕНО: Додано точну назву твого репозиторію "privid-app"
    web_app_info = types.WebAppInfo(url="https://secretniibreinrot-debug.github.io/privid-app/")
    btn_site = types.InlineKeyboardButton(text="👻 Відкрити ПРИВІД", web_app=web_app_info)
    
    markup.add(btn_site)
    
    welcome_text = "Привіт! Це мережа ПРИВІД. Твій надійний термінал розіграшів."
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

bot.polling(none_stop=True)
