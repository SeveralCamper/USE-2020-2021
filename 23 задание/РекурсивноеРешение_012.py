# Задание 23 № 18450
# Исполнитель преобразует число на экране.
# У исполнителя есть две команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Умножить на 2
# Первая команда увеличивает число на экране на 1, вторая умножает его на 2.
# Программа для исполнителя – это последовательность команд.
# Сколько существует программ, для которых при исходном числе 2 результатом является число 29 и при этом траектория
# вычислений содержит число 14?
# Траектория вычислений программы — это последовательность результатов выполнения всех команд программы. Например,
# для программы 121 при исходном числе 7 траектория будет состоять из чисел 8, 16, 17.

def RecFunc(x,y):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        return RecFunc(x + 1,y) + RecFunc(x*2,y)

print(RecFunc(2,14) * RecFunc(14,29))

# Ответ: 26