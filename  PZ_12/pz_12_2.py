# Составить список, в который будут включены только согласные буквы и привести их к верхнему регистру.
# Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир'].
from functools import reduce

words = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']


def filter_consonants(acc, word):
    consonants = 'БВГДЖЗКЛМНПРСТФХЦЧШЩЙ'
    filtered_word = ''
    for char in word:
        if char.upper() in consonants:
            filtered_word += char.upper()
    acc.append(filtered_word)
    return acc


filtered_words = reduce(filter_consonants, words, [])

print(filtered_words)
