# Задание 16 № 8099
# Ниже на пяти языках программирования записаны две рекурсивные функции (процедуры): F и G.

def F(n):
    if n > 0:
        G(n - 1)
 

def G(n):
    print("*")
    if n > 1:
        F(n - 2)
print(F(11))

# Ответ: 4
