# Задание 27 № 35916
# В текстовом файле записан набор натуральных чисел, не превышающих 108. Гарантируется, что все числа различны.
# Из набора нужно выбрать три числа, сумма которых делится на 3. Какую наименьшую сумму можно при этом получить?
# Входные данные.
# Файл A
# Файл B
# Первая строка входного файла содержит целое число N — общее количество чисел в наборе. Каждая из следующих N строк
# содержит одно число.
# В данном случае есть четыре подходящие тройки: 5, 8, 11 (сумма 24); 5, 8, 14 (сумма 27); 5, 14 11 (сумма 30) и 8, 14,
# 11 (сумма 33). В ответе надо записать число 24.
# Вам даны два входных файла (A и B), каждый из которых имеет описанную выше структуру. В ответе укажите два числа:
# сначала значение искомой суммы для файла A, затем для файла B.

data = open('011.txt').read().split()
a = []
minSum = 10000
for i in data:
    x = int(i)
    a.append(x)

for i in range(len(a)):
    for j in range(i + 1, len(a) - 1):
        for k in range(j + 1, len(a) - 2):
            if ((a[i] + a[j] + a[k]) % 3 == 0 and (a[i] + a[j] + a[k]) < minSum):
                minSum = (a[i] + a[j] + a[k])

print(minSum)

# Ответ: 327
