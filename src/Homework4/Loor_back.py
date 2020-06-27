"""
Оглянемся назад
Даны два натуральных числа.
Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""


def evklid(a, b):
    number_one = a
    number_two = b
    lst = []
    while a > 0:
        if b <= 0:
            break
        a = a % b
        if a <= 0:
            break
        elif b % a == 0:
            b = b // a
        else:
            b = b % a
        lst.append(a)
        lst.append(b)
    lst1 = []
    for el in lst:
        if el == 1:
            continue
        elif el in lst1:
            continue
        elif number_one % el == 0 and number_two % el == 0:
            lst1.append(el)
    return max(lst1)


if __name__ == '__main__':
    a, b = 432, 324
    print(evklid(a, b))
