def str_normalize(str_i):
    str_o = ''
    i = 0
    len_s = len(str_i)
    while i<len_s:
        i += 1
    return str_o

def find_md(str_i, pos=0, step=1):
    if str_i.find('*') != -1 \
        or str_i.find('/') != -1:
        while str_i[pos] not in '*/':
            pos += step
        return pos
    else:
        return 0

def find_pm(str_i, pos=0, step=1):
    sign = 0
    if pos == 0 and str_i[0] == '-':
        sign = 1
        str_i = str_i[1:]
    if str_i.find('+') != -1 \
        or str_i.find('-') != -1:
        while str_i[pos] not in '+-':
            pos += step
        return pos + sign
    else:
        return 0

def get_dig(str_i, pos=0, step=1):
    pos_start = pos
    if step == 1:
        if str_i[pos] == '-':
            pos += step
    
    try:
        while str_i[pos] in '0123456789.':
            pos += step
            if pos < 0:
                break
    except IndexError:
        pass

    if step == 1:
        res = str_i[pos_start:pos]
        res_pos = pos
    else:
        if pos > 1:
            if str_i[pos-1] == '-' and str_i[pos-2] in '*/':
                pos += step
        elif pos == 0:
            if str_i[pos] == '-':
                pos += step
        res = str_i[pos+1:pos_start+1]
        res_pos = pos + 1
    return res, res_pos

def check_rules(str_i):
    #Строка не может начинаться с * или / не может заканчиваться * / + - . и перечисление недопустимого соседства
    if len(str_i) == 0:
        return 'Длина выражения равна нулю'
    elif set(str_i).isdisjoint('+-*/')\
        or str_i.rfind('-') == 0 and set(str_i).isdisjoint('+*/'):
            return 'Не найдено математических операций'
    elif str_i[0] in '*/+' \
        or str_i[-1] in '*/+-.' \
        or str_i.find('+/') != -1 \
        or str_i.find('-/') != -1 \
        or str_i.find('+*') != -1 \
        or str_i.find('-*') != -1 \
        or str_i.find('+-') != -1 \
        or str_i.find('-+') != -1 \
        or str_i.find('.+') != -1 \
        or str_i.find('.-') != -1 \
        or str_i.find('.*') != -1 \
        or str_i.find('./') != -1 \
        or str_i.find('**') != -1 \
        or str_i.find('*/') != -1 \
        or str_i.find('/*') != -1 \
        or str_i.find('//') != -1 \
        or str_i.find('/+') != -1 \
        or str_i.find('*+') != -1:
            return "недопустимое выражение"
    else:
        return ''

def strip_value(str_i, pos=0):
    #выделяем значение
    str_o = ''
    if str_i[pos] in '+-':
        str_o += str_i[pos]
        pos += 1
    while str_i[pos] in '0123456789.':
        str_o += str_i[pos]
        pos += 1
    #проверка на две . в значении
    if len([x for x in str_o if x == '.']):
        error = True
    else:
        error = False
    #возврат значения в числовом виде со знаком, позиции где закончилось значаение, и ошибки в значении
    return float(str_o), pos, error
'''
def split_string(str_i):
    list_o = []
    error = False
    pos = 0
    #el_sign = True
    if (str_i[0] in '+-') and (str_i[1] in '.0123456789'):
        val, pos, error = strip_value(str_i, 0)
        if not error:
            list_o.append(val)
        else:
            return error
    else:
        error = True
        return error
    len_s = len(str_i)
    while pos < len_s:
        val, pos, error = strip_op(str_i, pos)
        if not error:
            list_o.append(val)
        else:
            return error
        val, pos, error = strip_value(str_i, pos)
        if not error:
            list_o.append(val)
        else:
            return error
'''

str1 = '2+4.34 * -5*6.2/-3* -7/3.1'
#str1 = '-.3*.2+.2'
#str1 = '-17-5*6/3-2+4/2'
#str1 = 40 : 5 + 12 – 8 : 2

invalid_sym = ''.join(set(str1).difference('0123456789+-*/. '))
if invalid_sym =='':
    norm_s = ''.join([x for x in str1 if x in '0123456789+-*/.'])
    print(str1)
    check_result = check_rules(norm_s)
    if check_result != '':
        print(check_result)
    else:
        print("выражение корректно")
        #split_string(norm_s)
        #norm_s = strip_signs(norm_s) Нужно описать функцию убирающие -
        #norm_s = ''.join([x for x in str1 if x in '0123456789+-*/.='])

        #проход 1 - умножение и деление
        print(norm_s)
        act_pos = find_md(norm_s)
        while act_pos != 0:
            #print(act_pos)
            act = norm_s[act_pos]
            #print(act)
            str_b, pos_b = get_dig(norm_s, find_md(norm_s)+1, 1)
            #b = ''.join(str_b)
            str_a, pos_a = get_dig(norm_s, find_md(norm_s)-1, -1)
            #a = ''.join(str_a)
            if act == '*':
                res = float(str_a)*float(str_b)
                print(str_a,act,str_b,'=',res)
            elif act == '/':
                res = float(str_a)/float(str_b)
                print(str_a,act,str_b,'=',res)
            norm_s = norm_s[:pos_a] + str(res) + norm_s[pos_b:]
            #print(norm_s)
            if norm_s.find('+-') != -1:
                norm_s = norm_s[:pos_a-1] + norm_s[pos_a:]
            elif norm_s.find('--') != -1:
                norm_s = norm_s[:pos_a-1] + '+' + norm_s[pos_a+1:]
            act_pos = find_md(norm_s)
            print(norm_s)

        #проход 2 - сложение и вычитание
        #print(norm_s)
        act_pos = find_pm(norm_s)
        while act_pos != 0:
            #print(act_pos)
            act = norm_s[act_pos]
            #print(act)
            str_b, pos_b = get_dig(norm_s, find_pm(norm_s)+1, 1)
            #b = ''.join(str_b)
            str_a, pos_a = get_dig(norm_s, find_pm(norm_s)-1, -1)
            #a = ''.join(str_a)
            if act == '+':
                res = float(str_a)+float(str_b)
                print(str_a,act,str_b,'=',res)
            elif act == '-':
                res = float(str_a)-float(str_b)
                print(str_a,act,str_b,'=',res)
            norm_s = norm_s[:pos_a] + str(res) + norm_s[pos_b:]
            #print(norm_s)
            act_pos = find_pm(norm_s)
            print(norm_s)

else:
    print('недопустимый символ', invalid_sym)
