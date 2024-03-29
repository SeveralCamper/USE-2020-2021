# Задание 23 № 23920
# Исполнитель Вычислитель преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Умножить на 2
# Первая команда увеличивает число на экране на 1, вторая умножает его на 2.
# Программа для Вычислителя — это последовательность команд. Сколько существует программ, для которых при исходном
# числе 1 результатом является число 21 и при этом траектория вычислений содержит число 10 и не содержит числа 18#
# Траектория вычислений программы — это последовательность результатов выполнения всех команд программы. Например,
# для программы 121 при исходном числе 7 траектория будет состоять из чисел 8, 16, 17.

def RecFunc(x,y):
    if x == y:
        return 1
    if x > y or x == 18:
        return 0
    if x < y:
        return RecFunc(x + 1,y) + RecFunc(x*2,y)

print(RecFunc(1,21))

# Ответ: 14