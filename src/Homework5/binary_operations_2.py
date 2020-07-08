"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def binary(int_):
    lst = []
    for degree in range(int_):
        degree_two = 2 ** degree
        if degree_two > int_:
            break
        if int_ % degree_two == 0:
            lst.append(degree_two)
    return max(lst)


if __name__ == '__main__':
    int_ = 16
    print(binary(int_))
