# Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Вывести строку, содержащую эти же слова, разделенные одним
# символом «.» (точка). В конце строки точку не ставить.
def join_words(string):
    words = string.split()  # Разделение строки на слова
    result = ".".join(words)  # Объединение слов с помощью точек
    return result

input_string = input("Введите строку: ")
new_string = join_words(input_string)
print(new_string)