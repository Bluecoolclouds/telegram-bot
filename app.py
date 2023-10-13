import telebot
import os
import openai
import time
import requests
import random
from flask import Flask
from modules import modules
from handlers.routes import configure_routes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('6556995841:AAE4ZccxFlpMzEtf1ZLGaDsbE13RYD-95D0')

bot = telebot.TeleBot(token=TOKEN, threaded=False)
app = Flask(__name__)
configure_routes(app, bot)


@bot.message_handler(commands=['start'])
def command_start(message):
    cid = message.chat.id
    bot.send_message(
        cid, "Welcome to putuwaw_bot!\nType /help to find all commands.")



