# Задание 24 № 27694
# Текстовый файл состоит не более чем из 106 символов A, B и C. Определите максимальную длину цепочки вида ABABAB...
# (составленной из фрагментов AB, последний фрагмент может быть неполным).
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с
# помощью данного алгоритма.

data = open('008-13.txt').read().strip()
count = 1
maxCount = 1
for i in range(len(data) - 1):
    if ((data[i] == 'A' and count % 2 == 0) or
    (data[i] == 'B' and count % 2 == 1)):
        count += 1
    elif(data[i] == 'A'):
        count = 1
    else:
        count = 0
    if (count > maxCount):
        maxCount = count
print(maxCount)

# Ответ: 24


