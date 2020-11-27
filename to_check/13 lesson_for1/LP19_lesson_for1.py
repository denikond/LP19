import random
import numpy
from decimal import Decimal

random.seed()
#Создать список из десяти целых чисел.
mas = [random.randint(0, 100) for x in range(10)]

#Вывести на экран каждое число, увеличенное на 1.
mas1 = [x+1 for x in mas]
print(mas1)

#Ввести с клавиатуры строку.
str1 = input("Введите строку\n")

#Вывести эту же строку вертикально: по одному символу на строку консоли.
for x in range(len(str1)):
    print(str1[x])

#Создать список из словарей с оценками учеников разных классов школы вида 
# [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]


clases = 4
letters = 'абв'
scores = 5
max_scor = 5
min_scor = 2

sch = []
for cl in range(1, clases):
    for let in range(random.randint(1, len(letters))):
        sc = [random.randint(min_scor, max_scor) for x in range(scores)]
        c1 = str(cl) + letters[let]
        #print('school_class', c1, 'scores', sc)
        sch.append(dict(school_class=c1, scores=sc))
print(sch)

#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.

stats = []
for cl1 in range(len(sch)):
    c1 = sch[cl1]['school_class']
    m1 = numpy.mean(sch[cl1]['scores'])
    stats.append(dict(school_class=c1, scores=m1))
    #print(c1,m1)
#print(stats)
print('Средняя успеваемость по классам')
#Вариант один
#[print(stats[x]['school_class'], ":", stats[x]['scores']) for x in range(len(stats))]

#Вариант два
#[print('{0} : {1}'.format(stats[x]['school_class'], stats[x]['scores'])) for x in range(len(stats))]

#Вариант три
[print(f"{stats[x]['school_class']} : {stats[x]['scores']}") for x in range(len(stats))]


print('Средняя успеваемость по школе ', numpy.mean([stats[x]['scores'] for x in range(len(stats))]))
