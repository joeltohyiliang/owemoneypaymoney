
import os
import telebot

my_secret = os.environ['api']

bot = telebot.TeleBot(my_secret)

@bot.message_handler(commands=['hi'])
def greet(message):
  bot.reply_to(message,'harlor')
  
@bot.message_handler(commands=['harlor'])
def greet(message):
  bot.send_message(message.chat.id,'harlor1')

bot.polling()

