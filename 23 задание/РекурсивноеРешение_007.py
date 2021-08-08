# Задание 23 № 10396
# Исполнитель Май16 преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Прибавить 2
# Первая команда увеличивает число на экране на 1, вторая увеличивает его на 2.
# Программа для исполнителя Май16 — это последовательность команд. Сколько существует программ, для которых при исходном
# числе 1 результатом является число 13 и при этом траектория вычислений содержит число 7, но не содержит числа 9?
# Траектория вычислений программы — это последовательность результатов выполнения всех команд программы.
# Например, для программы 121 при исходном числе 7 траектория будет состоять из чисел 8, 10, 11.

def RecFunc(x,y):
    if x == y:
        return 1
    if x > y or x == 9:
        return 0
    if x < y:
        return (RecFunc(x + 1, y) + RecFunc(x + 2, y))

print(RecFunc(1,7) * RecFunc(7,13))

# Ответ:39
