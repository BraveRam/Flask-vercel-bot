import telebot
from flask import Flask, request

TOKEN = '6064058058:AAFaGx_p7vqzEFiuxpdlSKTdEXdLdS9-pw0'  
bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()
webhook_url = 'https://flask-vercel-bot.vercel.app/' 
bot.set_webhook(url=webhook_url, drop_pending_updates=True)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
    return 'ok', 200 
