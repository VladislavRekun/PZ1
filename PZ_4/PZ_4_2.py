# Вторая задача
# Дано целое число N (N > 0). Если оно является степенью число 3, то вывести TRUE, если не является - вывести FALSE.
while True:
    try:
        n = int(input("Введите целое число n: "))
        a = int(input("a = "))
        sum = 0
        term = 0
    except ValueError:
        print("Что-то не так")
        continue
    break

st = 1

while st < a : st = st*3

print(st == n)
