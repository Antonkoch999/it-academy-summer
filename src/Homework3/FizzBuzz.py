"""Напишите программу, которая печатает цифры от 1
 до 100, но вместо чисел, кратных 3 пишет Fizz,
 вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно
 кратных и 3 и 5 - FizzBuzz"""


def fizzBuzz(int_):
    # n - количество чисел для цикла
    lst = []
    for i in range(1, int_ + 1):
        if not i % 3 and not i % 5:
            i = 'FizzBuzz'
            lst.append(i)
            continue
        if not i % 3:
            i = 'Fizz'
            lst.append(i)
            continue
        if not i % 5:
            i = 'Buzz'
            lst.append(i)
            continue
        else:
            lst.append(i)
    return lst


if __name__ == '__main__':
    int_ = int(input())
    print(fizzBuzz(int_))
