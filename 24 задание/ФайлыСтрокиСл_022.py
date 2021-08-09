# Задание 24 № 35482
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только
# заглавные буквы латинского алфавита (ABC…Z).
# Необходимо найти строку, содержащую наименьшее количество букв G (если таких строк несколько, надо взять ту, которая
# находится в файле раньше), и определить, какая буква встречается в этой строке чаще всего. Если таких букв несколько,
# надо взять ту, которая позже стоит в алфавите.
# Пример. Исходный файл:
# GIGA
# GABLAB
# AGAAA
# В этом примере в первой строке две буквы G, во второй и третьей — по одной. Берём вторую строку, т. к. она находится
# в файле раньше. В этой строке чаще других встречаются буквы A и B (по два раза), выбираем букву B, т. к. она позже
# стоит в алфавите. В ответе для этого примера надо записать B.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью
# данного алгоритма.

from collections import Counter
data = open('022.txt')
lines = data.readlines()
s = "G" * 1000
for line in lines:
    if line.count('G') < s.count('G'):
        s = line
print(Counter(s).most_common(1))