# Задание 16 № 7922
# Ниже на пяти языках программирования записан рекурсивный алгоритм F.
# Чему будет равно значение, вычисленное алгоритмом при выполнении вызова F(5)?

def F(n):
    if n > 2:
        return F(n-1)+ F(n-2)
    else:
        return n

print(F(5))

Ответ: 8