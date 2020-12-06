import os
import random as random

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


def do_response(cities_set, letter):
    result = [ set_ for set_ in cities_set.keys() if cities_set[set_]['is_used'] == False and cities_set[set_]['first_lett'] == letter ]
    if len(result) == 0:
        return 0
    elif len(result) > 1:
        result = result[random.randrange(len(result))]
        return result
    

user_data = {}
#print(len(user_data.keys()))
user_data['cities_game'] = {}
user_data['cities_game']['cities_set'] = cities_init()
user_data['cities_game']['cities_first'] = 'в'
user_data['cities_game']['cities_last'] = 'ц'

#print(len(user_data.keys()))
#print(user_data)

#cities = user_data['cities_game'].keys()

print('cities_game' in user_data.keys())
#print(len(user_data['cities_game']))

#print(user_data['cities_game']['Абаза'])
"""
for set_ in user_data['cities_game']:
    print(set_, user_data['cities_game'][set_]['is_used'])
    user_data['cities_game'][set_]['is_used'] = True

for set_ in user_data['cities_game']:
    print(set_, user_data['cities_game'][set_]['is_used'])
    
for set_ in user_data['cities_game']['cities_set']:
    if  user_data['cities_game']['cities_set'][set_]['is_used'] == False and user_data['cities_game']['cities_set'][set_]['first_lett'] == user_data['cities_game']['cities_last']:
        print(set_)
"""
print(do_response(user_data['cities_game']['cities_set'], 'ы'))


#print('Абакан' in cities)
#print(user_data['cities_game'])
