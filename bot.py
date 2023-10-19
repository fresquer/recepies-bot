import os
import inspect
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from helpers import getFomratedMessage, getRecepieFormated
from notion import get_page, get_recepie_by_momento

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
    message = getFomratedMessage(content)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=inspect.cleandoc(message))

async def randomFnCena(update: Update, context: ContextTypes.DEFAULT_TYPE):
    content = get_recepie_by_momento('cena')
    message = getFomratedMessage(content)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=inspect.cleandoc(message))

async def randomFnComida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    content = get_recepie_by_momento('comida')
    message = getFomratedMessage(content)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=inspect.cleandoc(message))


if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start', start)
    random_handler = CommandHandler('random', randomFn)
    cena_handler = CommandHandler('cena', randomFnCena)
    comida_handler = CommandHandler('comida', randomFnComida)


    application.add_handler(start_handler)
    application.add_handler(random_handler)
    application.add_handler(cena_handler)
    application.add_handler(comida_handler)
    
    application.run_polling()