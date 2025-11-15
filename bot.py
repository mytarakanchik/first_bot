import telebot
import random
import os

TOKEN = os.getenv("BOT_TOKEN")  # переменная окружения на Render

bot = telebot.TeleBot(TOKEN)

support_phrases = [
    "Дорогу одолеет идущий",
    "Неидеальное действие лучше идеального бездействия",
    "Поражение или ошибки — это плата за успех",
    "Несмотря на весь пиздец — ты сегодня молодец",
    "Ты — это самый главный проект в жизни, над которым ты работаешь",
    "Не бойся будущего — оно не настоящее",
    "Просто делай как получается, а Вселенная разберется",
    "Сколько раз ты готова была сдаться — столько раз решала продолжать",
    "Помни, что ты Дашулька-красотулька",
    "Все будет хорошо, я это знаю"
]

trigger_phrases = [
    "мне грустно", "поддержи меня", "я устала",
    "грустно", "мне плохо", "тяжело"
]

@bot.message_handler(func=lambda message: True)
def respond(message):
    text = message.text.lower()
    if any(trigger in text for trigger in trigger_phrases):
        bot.send_message(message.chat.id, random.choice(support_phrases))

# Убираем webhook и запускаем polling
bot.remove_webhook()
bot.polling(none_stop=True)
