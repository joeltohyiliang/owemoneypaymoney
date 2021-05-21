
import os
import requests
import telebot


my_secret = os.environ['api']

bot = telebot.TeleBot(my_secret)

@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message,'lets start')

@bot.message_handler(commands=['hi'])
def greet(message):
  bot.reply_to(message,'harlor')
  
@bot.message_handler(commands=['harlor'])
def greet2(message):
  bot.send_message(message.chat.id,'harlor1')

@bot.message_handler(commands=['help'])
def greet3(message):
  bot.send_message(message.chat.id,'help is here')

# def help(update, context):
#     """Send a message when the command /help is issued."""
#     update.message.reply_text('Help!')


# def echo(update, context):
#     """Echo the user message."""
#     update.message.reply_text(update.message.text)


# def error(update, context):
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, context.error)


bot.polling()

