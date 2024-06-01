# Сгенерировать матрицу на произвольное количество элементов, в которой задается
# преобразование от предыдущего элемента к следующему на произвольное значение.
import random

n = random.randint(1,3)
N = random.randint(3,8)
M = random.randint(3,8)
matr = [[M*i*n + n*j for j in range(M)] for i in range(N)]

print(matr)