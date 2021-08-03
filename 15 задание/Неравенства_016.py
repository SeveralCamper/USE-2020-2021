# Задание 15 № 18087
# Для какого наименьшего целого неотрицательного числа A выражение
# (y + 2x < A) ∨ (x > 15) ∨ (y > 30)
# тождественно истинно при всех вещественных значениях x и y?

A = 1
while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((y + 2*x < A) or (x > 15) or (y > 30)):
                break
        else:
            continue
        break
    else:
        print(A)
    A += 1

# Ответ: 61