"""
Оглянемся назад
Даны два натуральных числа.
Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""


def evklid(a, b):
    if a < b:
        a, b = b, a
    while a > 0:
        if b <= 0:
            break
        a = a % b
        if a <= 0:
            break
        b = b % a
    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':
    a, b = 594, 7920
    print(evklid(a, b))
