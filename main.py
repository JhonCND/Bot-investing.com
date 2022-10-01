import telebot
from web import webscraping
from help import helping
from modo_velho import web
from cambio2 import cambio

#FUNÇAOES
modovelho = web()
wweb = webscraping()
    #Token
TOKEN = ("key")
bot = telebot.TeleBot('1694856172:AAELynQUXMIMxKx2FdL4p7i9i0uJTbLalKI')
    #Commands
@bot.message_handler(commands=['start'])
def send_welcome(message):
     bot.reply_to(message, wweb)
    #Help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, helping)

@bot.message_handler(commands=['start2'])
def send_welcome(message):
    bot.reply_to(message, modovelho)

@bot.message_handler(commands=['cambio'])
def send_welcome(message):
     bot.reply_to(message,cambio)
    #Loop
bot.polling()