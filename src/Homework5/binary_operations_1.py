"""
Написать программу которая находит ближайшую
степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


def binary(int_):
    counter = 0

    while (int_ >> counter) > 1:
        counter += 1

    if (int_ - (2 ** counter)) < (2 ** (counter + 1) - int_):
        return 2 ** counter
    else:
        return 2 ** (counter + 1)


if __name__ == '__main__':
    int_ = 10
    print(binary(int_))
