"""
Определения:
Шоколадка - прямоугольник, размером n×m (n, m - натуральные).
Разлом - деление шоколадки на две части с натуральными размерами по прямой.
Долька - элемент шоколадки размером 1х1.
Очевидно шоколадка состоит из n*m долек.
Кусок - элемент шоколадки произвольного (целочисленного размера).

1. Определите, можно ли одним разломом отделить от шоколадки
кусок площадью ровно k.
2. Определите, можно ли отломить от шоколадки ровно k долек
за некоторое количество разломов.
3. Определите, можно ли отломить от шоколадки ровно k
долек с помощью t разломов
"""


def chocolate1(m, n, k, t):
    a = k / n
    b = k / m
    if a in range(1, m) or b in range(1, n):
        return 'Можно'
    else:
        return 'Нельзя'


def chocolate2(m, n, k, t):
    a = m
    b = n
    c = k
    if (k % n == 0 or k % m == 0) and k <= n * m:
        return 'Можно'
    while k > 0:
        if (k % n == 0 or k % m == 0) and k <= n * m:
            return 'Можно'
        else:
            k = k - n
            m = m - 1
    while c > 0:
        if (c % b == 0 or c % a == 0) and c <= b * a:
            return 'Можно'
        else:
            c = c - a
            b = b - 1
    return 'Нельзя'


def chocolate3(m, n, k, t):
    a = m
    b = n
    c = k
    d = t
    if (k % n == 0 or k % m == 0) and k <= n * m:
        return 'Можно'
    while k > 0:
        if (k % n == 0 or k % m == 0) and k <= n * m:
            return 'Можно'
        else:
            k = k - n
            m = m - 1
    while c > 0:
        if (c % b == 0 or c % a == 0) and c <= b * a:
            return 'Можно'
        else:
            c = c - a
            b = b - 1
    return 'Нельзя'


if __name__ == '__main__':
    m, n, k, t = 6, 4, 14, 5
    print(chocolate1(m, n, k, t))
    print(chocolate2(m, n, k, t))
    print(chocolate3(m, n, k, t))
