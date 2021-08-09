# [2532000;2532160] Найти все простые числа в диапозоне
# В ответ только каждое третье. Простое - значит не делится на что либо, кроме себя

a = []
num = 1
for x in range(2532000,2532160):
    flag = True
    for i in range(2, int(x ** 0.5) + 1):
        if (x % i == 0):
            flag = False
            break
    if (flag):
        a.append([num, x])
        num += 1
print(sorted(a[::3]))

