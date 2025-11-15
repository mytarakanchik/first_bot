from flask import Flask
import telebot
import random
import os
import threading

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

support_phrases = [
    "Дорогу одолеет идущий",
    "Неидеальное действие лучше идеального бездействия",
    "Поражение или ошибки — это плата за успех",
]

trigger_phrases = ["мне грустно", "поддержи меня", "я устала"]

@bot.message_handler(func=lambda message: True)
def respond(message):
    text = message.text.lower()
    if any(trigger in text for trigger in trigger_phrases):
        bot.send_message(message.chat.id, random.choice(support_phrases))

# Запускаем бота в отдельном потоке
threading.Thread(target=bot.infinity_polling, daemon=True).start()

# Мини-сервер для Render
app = Flask("")

@app.route("/")
def home():
    return "Bot is running!"

# Render требует PORT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
