+from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import logging
from datetime import datetime, timedelta
import locale,ephem

logging.basicConfig(filename="mybot.log", level=logging.INFO)

def mysplit(str1): #Функция для деления предложения на слова принимает str, возвращает list
    word_component = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #str1 = '  У  луркоморья дуб , зеленый,злотая цепь на дубе то м'
    i = 0
    strlen = len(str1) - 1
    strlist = []
    not_end = True
    while i < strlen and not_end:
        if str1[i] not in word_component:
            i = i + 1
        else:
            j = i
            while str1[j] in word_component and not_end:
                if j < strlen:
                    j += 1
                else:
                    not_end = False
            if not_end:
                strlist.append(str1[i:j])
            else:
                strlist.append(str1[i:j+1])
            i = j
    if str1[i] in word_component and str1[i-1] not in word_component:
        strlist.append(str1[i])
    return strlist



def talk_to_me(update, context):
    text = update.message.text
    if text == "o/":
        text = "\o"
    update.message.reply_text(text)
    

def greet_user(update, context):
    #print("вызван /start")
    #print(update)
    update.message.reply_text("я поддерживаю следующие команды")
    update.message.reply_text("/wordcount <строка>")
    update.message.reply_text("/next_full_moon YYYY-MM-DD")

def next_full_moon(update, context): #Функция возвращающая ближайшее полнолуние
    locale.setlocale(locale.LC_ALL, "russian")
    text = update.message.text
    spl = text.split()
    try:
        dt = datetime.strptime(spl[1], '%Y-%m-%d')
    except ValueError:
        update.message.reply_text("Введен неверный формат даты. Поддерживается YYYY-MM-DD")
    else:
        out_text = str(ephem.next_full_moon(dt))
        update.message.reply_text(out_text)

def wordcount(update, context): #Функция возвращающая количество слов в предложении
    text = update.message.text
    spl = mysplit(text)
    word_count = len(spl) - 1
    out_text = str(word_count) + ' слов(а)'
    update.message.reply_text(out_text)

""" кусок выпилен за ненадобностью

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
"""

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    #dp.add_handler(CommandHandler("planet", planet_const))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info(str(datetime.now()) +" Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
