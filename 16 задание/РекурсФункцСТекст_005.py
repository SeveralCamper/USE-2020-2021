# Задание 16 № 9163
# Ниже на пяти языках программирования записан рекурсивный алгоритм F.
# Чему равна сумма всех чисел, напечатанных на экране при выполнении вызова F(1)?

count = 0

def F(n):
    global count
    count += n
    print(n)
    if n < 4:
        F(n + 1)
        F(n + 3)

print(F(1), count)

# Ответ: 25