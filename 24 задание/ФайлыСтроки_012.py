# Задание 24 № 27693
# Текстовый файл состоит не более чем из 106 символов A, B и C. Определите максимальное количество идущих подряд
# символов C.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с
# помощью данного алгоритма.

data = open('008-13.txt').read().strip()
count = 1
maxCount = 1
for i in range(len(data) - 1):
    if (data[i] == 'C' and data[i] == data[i-1]):
        count += 1
    else:
        count = 1
    if (count > maxCount):
        maxCount = count

print(maxCount)

# Ответ: 1