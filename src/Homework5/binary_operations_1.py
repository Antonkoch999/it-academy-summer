"""
Написать программу которая находит ближайшую
степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


def binary(int_):
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


if __name__ == '__main__':
    int_ = 13
    print(binary(int_))
