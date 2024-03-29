#  Задание 23 № 16825
# Исполнитель РазДваТри преобразует число на экране.
# У исполнителя есть три команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Умножить на 2
# 3. Прибавить 3
# Первая команда увеличивает число на экране на 1, вторая умножает его на 2, третья увеличивает на 3.
# Программа для исполнителя РазДваТри — это последовательность команд.
# Сколько существует программ, которые преобразуют исходное число 3 в число 16 и при этом
# траектория вычислений не содержит чисел 6 и 12?
# Траектория вычислений — это последовательность результатов выполнения всех команд программы. Например,
# для программы 312 при исходном числе 6 траектория будет состоять из чисел 9, 10, 20.

def RecFunc(x,y):
    if x == y:
        return 1
    if x > y or x == 6 or x == 12:
        return 0
    if x < y:
        return RecFunc(x + 1,y) + RecFunc(x*2,y) + RecFunc(x+3,y)

print(RecFunc(3,16))

# Ответ: 22