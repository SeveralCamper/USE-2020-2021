# Задание 16 № 10501
# Ниже на пяти языках программирования записана рекурсивная функция (процедура) F.
# Что выведет программа при вызове F(4)? В ответе запишите последовательность выведенных цифр слитно (без пробелов).

def F(n):
    print (n, end='')
    if n > 2:
        F(n - 1)
        F(n - 2)
        F(n - 3)

print(F(4))

# Ответ: 4321021