"""
Написать программу которая находит ближайшую
степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


def binary(int_=20):

    lst = []
    for degree in range(int_):
        degree_two = 2 ** degree
        if degree_two < int_:
            lst.append(degree_two)
        else:
            lst.append(degree_two)
            break
    lst1 = [abs(x - int_) for x in lst]
    index_ = lst1.index(min(lst1))
    return lst[index_]


"""
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def pair_el(str_='1 1 1 1'):

    count = 0
    lst = str_.split(' ')
    for el in range(len(lst)):
        value = lst[el]
        pairs = lst[el + 1:].count(value)
        count += pairs
    return count
