# Даны два числа. Вывести порядковый номер меньшего из них.
while True:
    try:
        a = int(input("Ввести первое число для второй задачи: "))
        b = int(input("Ввести второе число для второй задачи: "))
    except ValueError:
        print("Что-то пошло не так")
        continue
    break

# Поиск меньшего числа во второй задачи
c = (1 if a<b else 2)

# ответ второй задачи
print("Ответ второй задачи")
print(c)