import logging, datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename="mybot.log", level=logging.INFO)

def talk_to_me(update, context):
    text = update.message.text
    if text == "o/":
        text = "\o"
    update.message.reply_text(text)
    

def greet_user(update, context):
    print("вызван /start")
#    print(update)
    update.message.reply_text("Здравствуй и прощай")

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info(str(datetime.datetime.now()) +" Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
