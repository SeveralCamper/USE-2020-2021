# Задание 17 № 33189
# Назовём натуральное число подходящим, если ровно два из его делителей входят в список (11, 13, 17, 19).
# Определите количество подходящих чисел, принадлежащих отрезку [11 000; 22 000], а также наименьшее из таких чисел.
# В ответе запишите два целых числа: сначала количество, затем, без разделительных знаков, наименьшее число.

count = 0
countDiv = 0
min= 22001
for x in range(11000,22001):
     countDiv = 0
     print("X",x)
     if x % 11 == 0:
          print("CD1", countDiv)
          countDiv += 1
     if x % 13 == 0:
          print("CD2", countDiv)
          countDiv += 1
     if x % 17 == 0:
          print("CD3", countDiv)
          countDiv += 1
     if x % 19 == 0:
         print("CD4", countDiv)
         countDiv += 1
     print("CD",countDiv)
     if (countDiv == 2):
        count += 1
        if (x < min):
            min = x
            print("MIN",min)
x += 1
print(count,min)

Ответ: 27311011
