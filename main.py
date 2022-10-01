import telebot
import requests
from bs4 import BeautifulSoup
import requests
from web import webscraping
from help import helping
from modo_velho import web
from cambio2 import cambio

#FUNÇAOES
kk = web()
texto = webscraping()
    #Token
TOKEN = ("key")
bot = telebot.TeleBot(TOKEN)
    #Commands incialiaçao
@bot.message_handler(commands=['start'])
def send_welcome(message):
     bot.reply_to(message,texto)
    #Help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, helping)
    #StartAntingo
@bot.message_handler(commands=['start2'])
def send_welcome(message):
    bot.reply_to(message, kk)
    #Cambio
@bot.message_handler(commands=['cambio'])
def send_welcome(message):
     bot.reply_to(message,cambio)
    #Loop
bot.polling()