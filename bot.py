from telegram.ext import Updater, CommandHandler
from telegram import Update
import os

def start(update: Update, context):
    update.message.reply_text("✅ Бот запущен через Railway!")

def repo(update: Update, context):
    update.message.reply_text("https://github.com/leshaprima/Quantum-Mirror-Lab")

TOKEN = os.environ['TELEGRAM_TOKEN']
updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("repo", repo))

print("Бот работает!")
updater.start_polling()
updater.idle()
