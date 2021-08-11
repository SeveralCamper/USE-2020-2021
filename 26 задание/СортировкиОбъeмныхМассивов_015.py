# Задание 26 № 35484
# В текстовом файле записан набор натуральных чисел, не превышающих 109. Гарантируется, что все числа различны.
# Необходимо определить, сколько в наборе таких пар чётных чисел, что их среднее арифметическое тоже присутствует в
# файле, и чему равно наибольшее из средних арифметических таких пар.
# Входные данные.
# Задание 26
# Первая строка входного файла содержит целое число N — общее количество чисел в наборе. Каждая из следующих N строк
# содержит одно число.
# В ответе запишите два целых числа: сначала количество пар, затем наибольшее среднее арифметическое.

data = open('015.txt')
count = 0
maxValue = 0
Mas = []
o = set()
plentyMas = set(Mas)
for i in data:
    x = int(i)
    if (x % 2 == 0):
        Mas.append(x)
    else:
        o.add(x)

for i in range(len(Mas)-1):
    for j in range(i + 1, len(Mas)):
        midValue = (Mas[i] + Mas[j]) // 2
        if (midValue in plentyMas) or (midValue in o):
            count += 1
            if midValue > maxValue:
                maxValue = midValue
print(count,maxValue)

# Ответ: 7 976339247 (Только один балл >:( )

# def BinarySearch(left,right,midValue,massive):
#     mid = 0
#     while(right > left + 1):
#         mid = (right + left) // 2
#         if (massive[mid] > midValue):
#             right = mid
#         elif(massive[mid] < midValue):
#              left = mid
#         else:
#             BinarySearch = True
#             break
#     BinarySearch = False
#
# data = open('015.txt')
# count = 0
# a = []
# maxValue = 0
# for i in data:
#     x = int(i)
#     a.append(int(x))
#
# a = sorted(a)
#
# for j in range(0, len(a) - 1):
#     MidValue = 0
#     if (a[j] % 2 == 0):
#         for k in range(j + 1, len(a) - 1):
#             if (a[k] % 2 == 0):
#                 MidValue = (a[j]+a[k])//2
#                 if BinarySearch(j,k,MidValue,a) == False:
#                     count += 1
#                     print('K.O.')
#                     if MidValue > maxValue:
#                         maxValue = MidValue
#                         print('Fatality')
#
# print(count,maxValue) Прекрасно, но не работает :\

# data = open('015.txt')
# N = int(data.readline())
# count = MaxValue = 0
# m = []
# s = []
# for i in data:
#     x = int(i)
#     s.append(int(x))
# s.sort()
# for i in range(N-1):
#     for j in range(i+1,N):
#         if s[i] % 2 == 0 and s[j] % 2 == 0:
#             m.append((s[i] + s[j]) // 2)
# m = set(m)
# m = sorted(m)
#
# for  i in range(len(m)):
#     j = 0
#     while m[i] > s[j]:
#         j += 1
#     if (m[i] == s[j]):
#         count += 1
#         MaxValue = max(MaxValue,m[i])
#
# print(s)
# print(m)
# print(MaxValue, count) Тоже не работает ://////

# Ответ: 15 976339247