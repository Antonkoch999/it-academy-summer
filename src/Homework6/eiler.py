"""Проект Эйлера. Задача 457.
'Многочлен по модулю квадрата простого числа'
Обобщите указанную задачу на свое усмотрение, решите ее, покройте тестами. """


def func(n=0):
    a = list(range(n + 1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1

    sum_lst = 0
    for simple_number in lst:
        for el in range(simple_number*simple_number):
            if ((el * el) - (3 * el) - 1) % (simple_number *
                                             simple_number) == 0:
                sum_lst += el
                break

    return sum_lst
