"""
Write a function, persistence, that
takes in a positive parameter num and
returns its multiplicative persistence,
which is the number of times you must multiply
the digits in num until you reach a single digit.

For example:

persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
# and 4 has only one digit.

Codewars lvl 6
"""


def persistence(n):
    count = 0
    if not n:
        return 0
    while n >= 10:
        k = 1
        count += 1
        for el in str(n):
            k *= int(el)
        n = k
    return count


if __name__ == '__main__':
    n = 39
    print(persistence(n))
