"""
Оглянемся назад
Даны два натуральных числа.
Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""


def evklid(number1, number2):

    while number1 and number2:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return number1 + number2


if __name__ == '__main__':
    number1, number2 = 50, 130
    print(evklid(number1, number2))
