"""
Даны два списка чисел. Посчитайте,
сколько различных чисел входит только
в один из этих списков
"""


def lists(lst1, lst2):
    st1 = set(lst1)
    st2 = set(lst2)
    st = st1 ^ st2
    return len(st)


if __name__ == '__main__':
    lst1 = [1, 2, 3, 7, 9]
    lst2 = [1, 2, 3, 8, 5]
    print(lists(lst1, lst2))
