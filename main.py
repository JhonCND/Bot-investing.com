import telebot
import requests
from bs4 import BeautifulSoup
import requests
from web import webscraping
from help import helping
from modo_velho import web
from boot import boo

#FUNÇAOES
kk = web()
texto = webscraping()
    #Token
TOKEN = ("1694856172:AAELynQUXMIMxKx2FdL4p7i9i0uJTbLalKI")
bot = telebot.TeleBot(TOKEN)
    #Commands
@bot.message_handler(commands=['start'])
def send_welcome(message):
     bot.reply_to(message, texto)
    #Help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, helping)

@bot.message_handler(commands=['start2'])
def send_welcome(message):
    bot.reply_to(message, kk)

@bot.message_handler(commands=['boot'])
def send_welcome(message):
     bot.reply_to(message,boo)
    #Loop
bot.polling()