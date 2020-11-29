from collections import Counter
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

result = Counter([student['first_name'] for student in students]).items()
for res in result:
    print(res[0], ':', res[1])

def search_often_name(students):
  result = list(Counter([student['first_name'] for student in students]).items())
  #print(result)
  max = result[0][1]
  idx_max = 1
  for idx, res in enumerate(result, start=1):
    if max < res[1]:
      idx_max = idx
      max = res[1]
  return result[idx_max-1][0]

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# Пример вывода:
# Самое частое имя среди учеников: Маша

print('Самое частое имя среди учеников:',search_often_name(students))


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]
# ???
for idx, students in enumerate(school_students):
    print('Самое частое имя в классе', idx+1, search_often_name(students))
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

def sex_calc(students, is_male):
    girls, boys = 0, 0
    for man in students:
        if is_male.get(man['first_name']):
            boys += 1
        else:
            girls += 1
    return girls, boys

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

for class_ in school:
    girls, boys = sex_calc(class_['students'], is_male)
    print('В классе', class_['class'], girls, 'девочки и', boys, 'мальчика')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
max_girls = 0
max_boys = 0
max_girls_class = ''
max_boys_class = ''

for class_ in school:
    girls, boys = sex_calc(class_['students'], is_male)
    if girls > max_girls:
        max_girls = girls
        max_girls_class = class_['class']
    if boys > max_boys:
        max_boys = boys
        max_boys_class = class_['class']
    
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
print('Больше всего мальчиков в классе', max_boys_class)
print('Больше всего девочек в классе', max_girls_class)


