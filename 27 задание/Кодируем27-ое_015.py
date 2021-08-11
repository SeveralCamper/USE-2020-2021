# Задание 27 № 36040
# Имеется набор данных, состоящий из троек положительных целых чисел. Необходимо выбрать из каждой тройки ровно одно
# число так, чтобы сумма всех выбранных чисел не делилась на k = 109 и при этом была максимально возможной.
# Гарантируется, что искомую сумму получить можно. Программа должна напечатать одно число — максимально возможную сумму,
# соответствующую условиям задачи.
# Входные данные.
# Файл A
# Файл B
# Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество троек N
# (1 ≤ N ≤ 1 000 000). Каждая из следующих N строк содержит три натуральных числа, не превышающих 20 000.
# Для указанных входных данных, в случае, если k = 5, значением искомой суммы является число 44.
# В ответе укажите два числа: сначала значение искомой суммы для файла А,
# затем для файла B.

data = open('015A.txt')
n = int(data.readline())
sum = 0
maxSum = 10000000
for i in range(n):
    a,b,c = data.readline().split()
    a = int(a)
    b = int(b)
    c = int(c)
    sum += max(a, b, c)
    n1 = max(a, b, c) - min(a, b, c)
    sr = a + b + c - max(a, b, c) - min(a, b, c)
    n2 = max(a, b, c) - sr
    if n1 % 109!= 0:
        maxSum = min(maxSum, n1)
    if n2 % 109!= 0:
        maxSum = min(maxSum, n2)
if sum % 109!= 0:
    print(sum)
else:
    print(sum - maxSum)


data = open('015B.txt')
n = int(data.readline())
sum = 0
maxSum = 10000000
for i in range(n):
    a,b,c = data.readline().split()
    a = int(a)
    b = int(b)
    c = int(c)
    sum += max(a, b, c)
    n1 = max(a, b, c) - min(a, b, c)
    sr = a + b + c - max(a, b, c) - min(a, b, c)
    n2 = max(a, b, c) - sr
    if n1 % 109!= 0:
        maxSum = min(maxSum, n1)
    if n2 % 109!= 0:
        maxSum = min(maxSum, n2)
if sum % 109!= 0:
    print(sum)
else:
    print(sum - maxSum)

# Ответ: 784594 8819088760

