# Задание 15 № 34508
# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n. Так, например, 14 & 5 = 11102 & 01012 = 01002 = 4. Для какого наименьшего неотрицательного целого числа А формула
# x & 29 ≠ 0 → (x & 12 = 0 → x & А ≠ 0)
# тождественно истинна (то есть принимает значение 1 при любом неотрицательном целом значении переменной х)?

A = 1
while True:
    for x in range(1, 100000):
        if not((x & 29 != 0) <= ((x & 12 == 0) <= (x & A != 0))):
            break
    else:
        print(A)
    A += 1

# Ответ: 17