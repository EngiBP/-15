import re

a = input("Введите имя файла")

myfile = open(a, 'rt', encoding='utf8')

file = myfile.readlines()

spisok_slov = []
for string in file:
    spisok_slov += string.split()

more_3_words = [x for x in spisok_slov if len(x)>3]

common_word_dict = {x:more_3_words.count(x) for x in more_3_words}

common_word = max(common_word_dict, key = common_word_dict.get)

r = re.compile('[a-zA-Z]+')

output = [w for w in filter(r.match, spisok_slov)]

english_longest_word = max(output, key=len)

print(f'Наиболее часто встречающееся слово из 3-х символов: {common_word}')
print(f'Самое длинное слово на английском языке: {english_longest_word}')

myfile.close()