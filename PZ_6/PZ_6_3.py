# Дано множество А из N точек на плоскости и точка В (точки заданы своими
# координатами х, у). Найти точку из множества А, наиболее близкую к точке В.
# Расстожше R между точками с координатами (XI, у) и (м, у) вычисляется по формуле: R = 4х2 - х1)2 + (у2 - у1)2.
#Для хранения данных о каждом наборе точек следует использовать по два списка: первый список для хранения абсцисс,
# второй — для хранения ординат.
import math


def find_closest_point(A, B):
    closest_point = None
    min_distance = float('inf')

    for i in range(len(A[0])):
        x = A[0][i]
        y = A[1][i]

        distance = math.sqrt((x - B[0]) ** 2 + (y - B[1]) ** 2)

        if distance < min_distance:
            min_distance = distance
            closest_point = (x, y)

    return closest_point


# Пример использования функции
A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
B = (2, 8)

closest_point = find_closest_point(A, B)
print("Ближайшая точка:", closest_point)