# Задание 24 № 33196
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего
# встречается в файле сразу после буквы A.
# Например, в тексте ABCAABADDD после буквы A два раза стоит B, по одному разу — A и D. Для этого текста ответом будет B.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью
# данного алгоритма.

data = open('018-20.txt')
a = [0] * 26
max = 0
for s in data:
    for i in range(len(s) - 1):
        if s[i] == 'A':
            a[ord(s[i + 1]) - 65] += 1 # тип ord - это расширение по таблице ASCII
for i in range(26):
    if a[i] > max:
        max = a[i]
        maxi = i
print(chr(maxi + 65))

# Ответ: G