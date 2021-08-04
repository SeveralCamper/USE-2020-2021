# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Так, например, 14 & 5 = 11102 & 01012 = 01002 = 4. Для какого наименьшего неотрицательного целого числа А формула
# x & 73 = 0 → (x & 28 ≠ 0 → x & А ≠ 0)
# тождественно истинна (т. е. принимает значение 1 при любом неотрицательном целом значении переменной x)?

A = 1
while True:
    for x in range(1, 1000000):
        if not((x & 73 == 0) <= ((x & 28 != 0) <= (x & A != 0))):
            break
    else:
        print(A)
    A += 1

# Ответ: 20