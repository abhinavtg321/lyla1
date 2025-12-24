from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Hello! I am your group management bot.")

def help_cmd(update, context):
    update.message.reply_text("/start\n/help\n/rules")

def rules(update, context):
    update.message.reply_text(
        "Group Rules:\n1. No spam\n2. Be respectful\n3. Follow admins"
    )

def welcome(update, context):
    for user in update.message.new_chat_members:
        update.message.reply_text(f"Welcome {user.first_name}!")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help_cmd))
dp.add_handler(CommandHandler("rules", rules))
dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

updater.start_polling()
updater.idle()
