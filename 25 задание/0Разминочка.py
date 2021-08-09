# [35612;57354] 25 делителей. Кол-во чисел и минимальное из них
# В ответ кол-во и мин. число

a = []
for x in range(35612, 57355):
    b = [1,x]
    for i in range(2, int(x ** 0.5) + 1):
        if (x % i == 0):
            b.append(i)
            b.append(x // i)
    b = set(b)
    if (len(b) >= 26):
        a.append(x)
print(len(a), min(a))

# Ответ: 1851 35616

