"""
Даны два списка чисел. Посчитайте,
сколько различных чисел содержится одновременно
как в первом списке, так и во втором.
"""


def lists_v1(lst1, lst2):
    lst1 = set(lst1)
    lst2 = set(lst2)
    res = lst1.intersection(lst2)
    return len(res)


if __name__ == '__main__':
    lst1 = [1, 2, 3, 7, 9]
    lst2 = [1, 2, 3, 8, 5]
    print(lists_v1(lst1, lst2))
