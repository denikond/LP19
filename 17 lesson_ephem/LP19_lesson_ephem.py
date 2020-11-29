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
    #выделяем имя планеты
    planet = update.message.text.split()[1]
    #Нормализуем ее вид (с большой буквы, остальные мал)
    planet = planet.capitalize()
    #выгружаем перечень объектов из ephem втроенной функцией
    ep_obj = ephem._libastro.builtin_planets()
    #оставляем только объекты с кодом Planet
    ep_planet = [ep_obj[x][2] for x in range(len(ep_obj)) if ep_obj[x][1] == 'Planet']
    #если то что ввели, соответствует одному элементу из библиотеки ephem с тегом Planet
    if planet in ep_planet:
        #формируем команду для получения объекта ephem.планета blah-bla
        comm = 'ephem.'+ planet + '(datetime.datetime.now())'
        #выполняем эту команду, получаем указатель на объект
        p_obj = eval(comm)
        #получаем созвездие
        constellation = ephem.constellation(p_obj)
        #Нормализуем вывод к правилам англ.языка
        if planet == 'Moon' or planet =='Sun':
            tex = 'The '
        else:
            tex = ''
        #Формируем вывод сообщения в человечесокм виде
        tex = tex + planet + ' is in ' + constellation[1] + ' constellation now.'
        #Выводим сообщение в канал чатбота
        update.message.reply_text(tex)
    else:
        #Выводим сообщение в канал чатбота
        update.message.reply_text("Unknown planet")


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
