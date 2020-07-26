"""
Создайте декоратор, который хранит результаты
вызовы функции (за все время вызовов,
не только текущий запуск программы)
"""


def dec(fun):

    def wrapper(args):
        print(f'Найти {args} число фибоначи')
        result = fun(args)
        with open('results.txt', 'a') as file:
            file.write(str(result) + '\n')
        return f'Результат вычисления: {fun(args)}'

    return wrapper


@dec
def func(n):
    fib1 = 1
    fib2 = 1
    while n:
        n -= 1
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


print(func(5))
print(func(10))
print(func(20))
