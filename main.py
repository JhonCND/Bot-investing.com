import telebot
from bs4 import BeautifulSoup
from web import webscraping
from help import helping
from modo_velho import web
from cambio2 import cambio

#FUNÇAOES
webtop = web()
webnovo = webscraping()
    #Token
TOKEN = ("1694856172:AAELynQUXMIMxKx2FdL4p7i9i0uJTbLalKI")
bot = telebot.TeleBot(TOKEN)
    #Commands incialiaçao
@bot.message_handler(commands=['start'])
def send_welcome(message):
     bot.reply_to(message,webnovo)
    #Help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, helping)
    #StartAntingo
@bot.message_handler(commands=['start2'])
def send_welcome(message):
    bot.reply_to(message, webtop)
    #Cambio
@bot.message_handler(commands=['cambio'])
def send_welcome(message):
     bot.reply_to(message,cambio)
    #Loop
bot.polling()