age_playsch_start = 3
age_playsch_stop = 7

age_school_start = 7
age_school_stop = 17

age_hi_school_start = 17
age_hi_school_stop = 65

age_work_start = 18
age_work_stop = 65


def what_can_i_do(age):
    you_do = []
    if (age<age_playsch_start):
        you_do.append("Лучше быть с мамой дома")
    if (age>=age_playsch_start) and (age<=age_playsch_stop):
        you_do.append("Можно быть в садике")
    if (age>=age_school_start) and (age<=age_school_stop):
        you_do.append("Можно быть в школе")
    if (age>=age_hi_school_start) and (age<=age_hi_school_stop):
        you_do.append("Можно быть в ВУЗе")
    if (age>=age_work_start) and (age<=age_work_stop):
        you_do.append("Можно работать")
    if (age>age_work_stop):
        you_do.append("Лучше отдохнуть")
    return you_do

age=int(input("Введите возраст "))
ido = what_can_i_do(age)
for i in range(len(ido)):
    print(ido[i])
