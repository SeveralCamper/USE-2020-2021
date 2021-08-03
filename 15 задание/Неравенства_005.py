# Задание 15 № 15113
# Сколько существует целых значений числа A, при которых формула
# ((x < A) → (x2 < 100)) ∧ ((y2 ≤ 64) → (y ≤ A))
# тождественно истинна при любых целых неотрицательных x и y?

A = 1
A_amount = 0
while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((not(x < A)) or (pow(x,2) < 100)) and ((not(pow(y,2) <= 64)) or (y <= A))):
                break
        else:
            continue
        break
    else:
        print(A)
        A_amount += 1
        print(A_amount)
    A += 1

# Ответ: 3
