# Задание 24 № 27689
# Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальную длину цепочки вида XYZXYZXYZ...
# (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью
# данного алгоритма.

data = open('004-7.txt').read().strip()
count = 0
maxCount = 0
for i in range(len(data) - 2):
    if ((data[i] == 'X' and count % 3 == 0)
    or data[i] == 'Y' and count % 3 == 1
    or data[i] == 'Z' and count % 3 == 2):
        count += 1
        if maxCount < count:
            maxCount = count
    elif (data[i] == 'X'):
        count = 1
    else:
        count = 0

print(maxCount)

# Ответ: 13