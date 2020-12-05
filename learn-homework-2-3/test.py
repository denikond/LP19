import os

def cities_init():
    #Функция инициализации игрового окружения игры в города
    cities_set = {}
    #считываем каталог городов
    print(os.getcwd())
    with open('d:/LP19/learn-homework-2-3/RU_cities.txt','r', encoding='utf-8') as fi:
        for line in fi:
            a = line.rstrip()
            cities_set[a] = { 'is_used' : False, 'first_lett' : a[0].lower(), 'last_lett' : (lambda x: x[-1] if x[-1] not in set('ьъ') else x[-2]) (a) }
            #cities_set[a] = 0, a[0].lower(), (lambda x: x[-1] if x[-1] not in set('ьъ') else x[-2]) (a)
        return cities_set

user_data = {}
#print(len(user_data.keys()))
user_data['cities_game'] = cities_init()
#print(len(user_data.keys()))
#print(user_data)

#cities = user_data['cities_game'].keys()

#print(user_data['cities_game'])
#print(len(user_data['cities_game']))

#print(user_data['cities_game']['Абаза'])

for set_ in user_data['cities_game']:
    print(set_, user_data['cities_game'][set_]['is_used'])
    user_data['cities_game'][set_]['is_used'] = True

for set_ in user_data['cities_game']:
    print(set_, user_data['cities_game'][set_]['is_used'])
    


#print('Абакан' in cities)
#print(user_data['cities_game'])
