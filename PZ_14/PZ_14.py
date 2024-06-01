# Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать
# количество полученных элементов.

import re

# Компилируем шаблон
st = re.compile(r"\d+\s*[(лет)*(год)*]+.*")

# Записываем файл в переменную
with open('experience.txt') as f1:
    exp_str = f1.read()

# Находи каждый стаж и их общее количество
lst1 = st.findall(exp_str)
exp_count = len(lst1)

# Вывод результата
print(lst1)
print(exp_count)
