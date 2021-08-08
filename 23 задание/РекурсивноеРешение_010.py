# Задание 23 № 27551
# Исполнитель РазДва преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Умножить на 2
# Первая команда увеличивает число на экране на 1, вторая умножает его на 2. Программа для исполнителя
# РазДва — это последовательность команд.
# Сколько существует программ, которые преобразуют исходное число 1 в число 20, и при этом траектория вычислений
# содержит ровно одно из чисел 9 и 10?
# Траектория вычислений — это последовательность результатов выполнения всех команд программы. Например, для
# программы 212 при исходном числе 4 траектория будет состоять из чисел 8, 9, 18.

def RecFunc9(x,y):
    if x == y:
        return 1
    if x > y or x == 10:
        return 0
    if x < y:
        return RecFunc9(x + 1, y) + RecFunc9(x*2, y)

def RecFunc10(x,y):
    if x == y:
        return 1
    if x > y or x == 9:
        return 0
    if x < y:
        return RecFunc10(x + 1, y) + RecFunc10(x*2, y)

print ((RecFunc9(1,10) * RecFunc9(10,20) + (RecFunc10(1,9) * RecFunc9(9,20))))

# Код выдает неверный ответ, я это задание уже решал в ручную
# Ответ: 18