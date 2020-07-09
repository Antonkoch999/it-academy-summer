"""Напишите программу, которая печатает цифры от 1
 до 100, но вместо чисел, кратных 3 пишет Fizz,
 вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно
 кратных и 3 и 5 - FizzBuzz"""


def fizzBuzz(n):
    # n - количество чисел для цикла
    for i in range(1, n + 1):
        if not i % 15:
            i = 'FizzBuzz'
            print(i)
        elif not i % 3:
            i = 'Fizz'
            print(i)
        elif not i % 5:
            i = 'Buzz'
            print(i)
        else:
            print(i)
    return ''


if __name__ == '__main__':
    n = 100
    print(fizzBuzz(n))
