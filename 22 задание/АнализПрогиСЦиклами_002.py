# Задание 22 № 18799
# Ниже на пяти языках программирования записан алгоритм. Получив на вход число x, этот алгоритм печатает два числа:
# L и M. Укажите наибольшее число x, при вводе которого алгоритм печатает сначала 3, а потом 7.

for i in range(1,20000):
    x = i
    L = 0
    M = 0
    while x > 0:
        M = M + 1
        if x % 2 != 0:
            L = L + 1
        x = x // 2
    if (L == 3 and M == 7):
        print(i)

# Ответ: 112