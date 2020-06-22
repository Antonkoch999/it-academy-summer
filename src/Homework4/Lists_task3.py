"""
Даны два списка чисел. Посчитайте,
сколько различных чисел содержится одновременно
как в первом списке, так и во втором.
"""


def lists_v1(lst1, lst2):
    counter = 0
    lst = []
    for item in lst1:
        if item in lst2 and item in lst:
            continue
        else:
            lst.append(item)
            counter += 1
    return counter


if __name__ == '__main__':
    lst1 = [1, 2, 3, 7, 9]
    lst2 = [1, 2, 3, 8, 5]
    print(lists_v1(lst1, lst2))
