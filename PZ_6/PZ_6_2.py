def check_permutation(lst):
    n = len(lst)
    visited = [False] * n

    for num in lst:
        if num < 1 or num > n or visited[num - 1]:
            return num
        visited[num - 1] = True

    return 0

# Пример использования функции
input_list = [4, 1, 3, 2, 5]
result = check_permutation(input_list)
print(input_list)
print(result)
