"""
Дан список стран и городов каждой страны.
Затем даны названия городов. Для каждого города укажите,
в какой стране он находится.
"""


import random


def cities(n, m):
    dct = {}
    lst = []

    for i in range(n):
        input_ = input('Введите страну и города:')
        dct[input_.split(' ')[0]] = input_.split(' ')[1:]

    for i in range(m):
        lst.append(random.choice(random.choice(list(dct.values()))))
    print(lst)
    for city in lst:
        for key, value in dct.items():
            if city in value:
                print(key)
    return ' '


if __name__ == '__main__':
    n, m = 2, 3
    print(cities(n, m))
