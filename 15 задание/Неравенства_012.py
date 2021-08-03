# Задание 15 № 16821
# Для какого наименьшего целого неотрицательного числа A выражение
# (3x + 4y ≠ 70) ∨ (A > x) ∨ (A > y)
# тождественно истинно при любых целых неотрицательных x и y?

A = 1
while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((3*x + 4*y != 70) or (A > x) or (A > y)):
                break
        else:
            continue
        break
    else:
        print(A)
    A += 1

# Ответ: 11