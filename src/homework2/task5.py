"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """

    # write your code here
    fib1 = 0
    fib2 = 1
    for i in range(1, n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 20
    print(fibonacci(n))
