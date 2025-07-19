import logging
from telegram.ext import *


logging.basicConfig(level=logging.INFO , format="%(asctime)s - %(name)s - %(message)s")

logging.info("her we goooooooooo ...")

API_KEY ='7607705113:AAG8pIYSvjS7tvmMPyVRdWj_ZuRZceXgJW4'

async def start_command(update ,context) :
    await update.message.reply_text("we are going to start")

async def help_command(update , context):
    await update.message.reply_text('what kinf of help do you need')

async def work_command(update , context):
    await update.message.reply_text('the work is done')

async def message_handler(update , context):
    entred_message = str(update.message.text).upper()
    logging.info(f"user {update.message.chat.id} said {entred_message}")
    await update.message.reply_text(f"{entred_message + ' ana grave harab'}")



def erreur_message(update , context):
    logging.error(f"something bad happened {context.erreur} ")



if  __name__ == '__main__':
    app = ApplicationBuilder().token(API_KEY).build()
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('awork',work_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND , message_handler))
    app.add_error_handler(erreur_message)
    app.run_polling()


