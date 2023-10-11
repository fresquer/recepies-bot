import os
import random
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from helpers import getRecepieFormated
from notion import get_page

load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')


import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def randomFn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    content = get_page()
    random_object = random.choice(content['results'])
    data = {"data": [getRecepieFormated(random_object)] }
    print(data)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Randommmmm")

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start', start)
    random_handler = CommandHandler('random', randomFn)

    application.add_handler(start_handler)
    application.add_handler(random_handler)
    
    application.run_polling()