from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

i = 0
updater = Updater(token='1414634833:AAFmJjgqm6zZgJP43de4eNomfD8WoWwqWvU', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
stop_commands = ['stop', 'stop copying me']

print("hello")
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    global i
    i = i+1
    if i==1:
        context.bot.send_message(chat_id=update.effective_chat.id, text='okay i will start copying you, to stop me say stop') 
    if update.message.text in stop_commands:
        context.bot.send_message(chat_id=update.effective_chat.id, text='okay i will not copy you')
        return 0
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()

