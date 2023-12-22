import telebot
from flask import Flask, request

TOKEN = '6064058058:AAFaGx_p7vqzEFiuxpdlSKTdEXdLdS9-pw0'  
bot = telebot.TeleBot(TOKEN)

webhook_url = 'https://your-webhook-url.com/webhook' 
bot.set_webhook(url=webhook_url)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
    return 'ok', 200 
