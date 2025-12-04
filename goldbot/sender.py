from .config import CHANNEL_ID



def send_messages(bot, message):
    """send message to Telegram channel"""
    bot.send_message(CHANNEL_ID, message)



