# Задание 15 № 14779
# Сколько существует целых значений числа A, при которых формула
# ((x < 5) → (x2 < A)) /\ ((y2 ≤ A) → (y ≤ 5))
# тождественно истинна при любых целых неотрицательных x и y?

A = 1
A_amount = 0
while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((not((x < 5)) or (pow(x,2) < A)) and (not(pow(y,2)) <= A) or (y <= 5)):
                break
        else:
            continue
        break
    else:
        print(A)
        A_amount += 1
        print(A_amount)
    A += 1

# Ответ: 19
