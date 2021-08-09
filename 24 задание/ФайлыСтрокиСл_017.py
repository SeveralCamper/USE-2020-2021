# Задание 24 № 33103
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только
# заглавные буквы латинского алфавита (ABC…Z). Определите количество строк, в которых буква A встречается чаще, чем буква E.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью
# данного алгоритма.

data = open('016-17.txt').read().split()
count = 0
for i in data:
    if i.count('A') > i.count('E'):
        count += 1
print(count)

# Ответ: 485