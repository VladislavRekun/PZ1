# В матрице найти сумму элементов первых двух строк.
import random

N = random.randint(3,5)
M = random.randint(3,5)
matr = [[random.randint(1,2) for j in range(M)] for i in range(N)]

print(matr)
print(sum((sum(matr[0]), sum(matr[1]))))