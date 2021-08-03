# Задание 15 № 13745
# Для какого наибольшего целого числа А формула
# ((x ≤ 9) →(x ⋅ x ≤ A)) ⋀ ((y ⋅ y ≤ A) → (y ≤ 9))
# тождественно истинна, то есть принимает значение 1 при любых целых неотрицательных x и y?

A = 1
while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if  not (((not(x <= 9)) or (x * x <= A)) and (not((y * y <= A)) or (y <= 9))):
                break
        else:
            continue
        break
    else:
        print(A)
    A += 1

# Ответ: 99



