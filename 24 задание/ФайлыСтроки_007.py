# Задание 24 № 27688
# Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите длину самой длинной последовательности,
# состоящей из символов Z. Хотя бы один символ Z находится в последовательности.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью
# данного алгоритма.

data = open('004-7.txt').read().strip()
count = 1
maxCount = 1
for i in range(len(data) - 1):
    if (data[i] == 'Z' and data[i] == data[i - 1]):
        count += 1
    else:
        count = 1
    if (count > maxCount):
        maxCount = count
print(maxCount)

# Ответ: 7