# Задание 15 № 17382
# Для какого наименьшего целого неотрицательного числа A выражение
# (5x + 3y ≠ 60) ∨ ((A > x) ∧ (A > y))
# тождественно истинно при любых целых неотрицательных x и y?

A = 1
while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((5*x + 3*y != 60) or ((A > x) and (A > y))):
                break
        else:
            continue
        break
    else:
        print(A)
    A += 1

# Ответ: 16 (21?)

