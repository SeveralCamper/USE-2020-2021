# Задание 24 № 27699
# Текстовый файл состоит не более чем из 106 символов L, D и R. Определите максимальную длину цепочки вида LDRLDRLDR...
# (составленной из фрагментов LDR, последний фрагмент может быть неполным).
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью
# данного алгоритма.

data = open('014.txt').read().strip()
count = 0
maxCount = 0
for i in range(len(data) - 1):
    if ((data[i] == 'L' and count % 3 == 0) or
    (data[i] == 'D' and count % 3 == 1) or
    (data[i] == 'R' and count % 3 == 2)):
        count += 1
    elif(data[i] == 'L'):
        count = 1
    else:
        count = 0
    if (count > maxCount):
        maxCount = count

print(maxCount)

# Ответ: 15
