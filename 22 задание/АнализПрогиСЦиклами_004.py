# Задание 22 № 6813
# Ниже на пяти языках записан алгоритм. Получив на вход число x, этот алгоритм печатает два числа: a и b.
# Укажите наименьшее из таких чисел x, при вводе которого алгоритм печатает сначала 3, а потом 4.

for i in range(1, 10000):
    x = i
    a = 0
    b = 0
    while x > 0:
        a += 1
        if b < (x % 8):
            b =x % 8
        x //=  8
    if (a == 3 and b == 4):
        print(i)
        break

# Ответ: 68
