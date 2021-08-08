# Задание № практика_6
# У исполнителя кальклятор есть три команды, которым присвоены номера:
# 1) +1
# 2) Добавить 1 к числу десятков, но если вторая с конца цифры = 9, ничего не изменится
# Сколько существует программ, которые число 10 преобразуют в 33?

def SecondFromEnd(n):
    if n//10 % 10 == 9:
        return n
    else:
        return n + 10

def RecFunc(x,y):
   if x == y:
       return 1
   if x > y:
       return 0
   if x < y:
       return RecFunc(x + 1, y) + RecFunc(SecondFromEnd(x), y)
print(RecFunc(10,33))


# Ответ: 25