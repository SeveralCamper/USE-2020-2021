# Задание № практика_1
# Дана цепочка из символов латинского алфавита A,B,C,D,E,F. Найдите длину самой длинной подцепочки, не содержащей
# гласных букв
# BBBCBCADDDADFFFFFFFE
# BСDDDADDDDDDFCDF

s = input()
n = len(s)
maxLenght = count = 0
for i in range(n):
    if(s[i] != 'A' and s[i] != 'E'):
        count += 1
    else:
        if (count > maxLenght):
            maxLenght = count
        count = 0
if (count > maxLenght):
    maxLenght = count
print(maxLenght)

# Ответ: 10 для BСDDDADDDDDDFCDF
#        8  для BBBCBCADDDADFFFFFFFE
