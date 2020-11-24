import logging, datetime, ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename="mybot.log", level=logging.INFO)

def talk_to_me(update, context):
    text = update.message.text
    if text == "o/":
        text = "\o"
    update.message.reply_text(text)
    

def greet_user(update, context):
    #print("вызван /start")
    #print(update)
    update.message.reply_text("Здравствуй и прощай")

def planet_const(update, context):
    #print("вызван /planet")
    planet = update.message.text.split()[1]
    planet = planet.capitalize() 
    p_obj = None
    if planet == 'Mercury':
        p_obj = ephem.Mercury(datetime.datetime.now())
    if planet == 'Venus':
        p_obj = ephem.Venus(datetime.datetime.now())
    if planet == 'Mars':
        p_obj = ephem.Mars(datetime.datetime.now())
    if planet == 'Jupiter':
        p_obj = ephem.Jupiter(datetime.datetime.now())
    if planet == 'Saturn':
        p_obj = ephem.Saturn(datetime.datetime.now())
    if planet == 'Uranus':
        p_obj = ephem.Uranus(datetime.datetime.now())
    if planet == 'Neptune':
        p_obj = ephem.Neptune(datetime.datetime.now())
    if planet == 'Pluto':
        p_obj = ephem.Pluto(datetime.datetime.now())
    if planet == 'Moon':
        p_obj = ephem.Moon(datetime.datetime.now())
    if p_obj is None:
        update.message.reply_text("Unknown planet")
    else:
        constellation = ephem.constellation(p_obj)
        if planet == 'Moon':
            tex = 'The Moon'
        else:
            tex = planet
        tex = tex + ' is in ' + constellation[1] + ' constellation now.'
        update.message.reply_text(tex)
        


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_const))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info(str(datetime.datetime.now()) +" Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
