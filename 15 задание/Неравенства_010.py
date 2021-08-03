# Задание 15 № 16393
# Для какого наименьшего целого неотрицательного числа A выражение
# (2x + 3y > 30) ∨ (x + y ≤ A)
# тождественно истинно при любых целых неотрицательных x и y?

A = 1
while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((2 * x + 3 * y > 30) or (x + y <= A)):
                break
        else:
            continue
        break
    else:
        print(A)
    A += 1

# Ответ: 14

