# Задание 15 № 15634
# Для какого наименьшего целого неотрицательного числа А выражение
# (y + 2x < A) ∨ (x > 30) ∨ (y > 20)
# тождественно истинно, то есть принимает значение 1 при любых целых неотрицательных x и y?

A = 1
while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((y + 2*x < A) or (x > 30) or (y > 20)):
                break
        else:
            continue
        break
    else:
        print(A)
    A += 1

# Ответ: 81