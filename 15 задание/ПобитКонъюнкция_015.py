# Задание 15 № 34517
# Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Так, например, 12&6 = 11002&01102 = 01002 = 4.
# Для какого наибольшего целого числа А формула
# х&А не равно 0 → (x&10 = 0 → х&3 не равно 0)
# тождественно истинна (т. е. принимает значение 1 при любом неотрицательном целом значении переменной x)?

A = 1
while True:
    for x in range (1, 100000):
        if not((x&A != 0) <= ((x&10 == 0) <= (x&3 != 0))):
            break
    else:
        print(A)
    A += 1

# Ответ: 11
