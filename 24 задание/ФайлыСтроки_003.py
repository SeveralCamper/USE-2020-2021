# Задание № практика_2
# Дана строка. Определите максимальное количество идущих подряд символов, среди которых каждые два различны
# axaxaaaaaqervbtweqrr

s = input()
n = len(s)
maxLength = count = 1
for i in range(n-1):
    if (s[i] != s[i+1]):
        count += 1
    else:
        if (count > maxLength):
            maxLength = count
        count = 1

print(maxLength)

# Ответ: 11


