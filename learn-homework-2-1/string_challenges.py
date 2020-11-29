# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print('Последняя буква в слове', word, word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print('Букв \'а\' в слове', word, word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
vowels = {'а', 'е', 'и', 'у', 'ы', 'о', 'э', 'я', 'ю'}
vowels_count = 0
for char_ in vowels:
    vowels_count += word.lower().count(char_)
print('Количество гласных букв в слове', word, vowels_count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print('Количество слов в предложении \'' + sentence + '\'', len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
for word in sentence.split():
    print(word[0])    

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# ???
word_mean_len = len(sentence.replace(' ', '')) / len(sentence.split())
print('Средняя длина слова', word_mean_len)
