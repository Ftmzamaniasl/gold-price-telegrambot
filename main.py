import telebot
import time 
from goldbot import sender, fetcher
from confing import TOKEN, API_KEY


def run_bot(invterval=10):
    while True:
        price = fetcher.fetch_gold_price(API_KEY)
        sender.send_messages(bot, price)
        time.sleep(invterval)


if __name__ == "__main__":
    bot = telebot.TeleBot(TOKEN)
    run_bot(invterval=300)
    bot.polling()