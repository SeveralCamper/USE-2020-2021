# Задание 22 № 11121
# Ниже на пяти языках программирования записан алгоритм. Получив на вход число x, этот алгоритм печатает два числа:
# a и b. Укажите наибольшее из таких чисел x, при вводе которых алгоритм печатает сначала 2, а потом 9.

for i in range(1, 10000):
    x = i
    a = 0
    b = 0
    while x > 0:
      a = a + 1
      b = b + (x % 10)
      x = x // 10
    if (a == 2 and b == 9):
        print(i)

# Ответ: 90