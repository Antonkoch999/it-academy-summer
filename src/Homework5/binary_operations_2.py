"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def binary(int_):
    counter = 0

    while (int_ >> counter >= 1) and (int_ % 2 ** counter == 0):
        counter += 1

    return 2 ** (counter - 1)


if __name__ == '__main__':
    int_ = 10
    print(binary(int_))
