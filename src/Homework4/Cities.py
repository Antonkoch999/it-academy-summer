"""
Дан список стран и городов каждой страны.
Затем даны названия городов. Для каждого города укажите,
в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия
страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M
запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны,
в котором находится данный город.
Примеры:
Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod
Выходные данные
Ukraine
Russia
Russia
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
    key_list = list(dct.keys())
    val_list = list(dct.values())
    for val in lst:
        for el in val_list:
            if val in el:
                print(key_list[val_list.index(el)])
    return ' '


if __name__ == '__main__':
    n, m = 2, 3
    print(cities(n, m))
