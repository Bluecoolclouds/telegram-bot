import telebot
import os




TOKEN = '6556995841:AAE4ZccxFlpMzEtf1ZLGaDsbE13RYD-95D0'

bot = telebot.TeleBot(token=TOKEN, threaded=False)


@bot.message_handler(commands=['start'])
def command_start(message):
    cid = message.chat.id
    bot.send_message(
        cid, "Welcome to putuwaw_bot!\nType /help to find all commands.")



