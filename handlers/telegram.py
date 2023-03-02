import os

import telebot
from dotenv import load_dotenv

load_dotenv()

def send_notify(message):
    # instead of os.environ.get('BOT_API_KEY') you can put api key from https://t.me/BotFather as string
    bot = telebot.TeleBot(os.environ.get('BOT_API_KEY'))
    # instead of os.environ.get('USER_CHAT_ID') you can put chat id from https://t.me/username_to_id_bot as int
    bot.send_message(os.environ.get('USER_CHAT_ID'), message)
