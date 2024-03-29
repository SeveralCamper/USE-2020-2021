# Задание 16 № 6423
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
# F(n) = n − 1 при n ≤ 2;
# F(n) = 3 × F(n − 1) − F(n − 2) при n> 2.
# Чему равно значение функции F(6)? В ответе запишите только натуральное число.

def F(n):
    if n <= 2:
        return n - 1
    else:
        return 3 * F(n - 1) - F(n - 2)

print(F(6))

# Ответ: 55