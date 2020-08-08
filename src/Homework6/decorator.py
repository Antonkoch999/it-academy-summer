"""
Создайте декоратор, который вызывает задекорированную
функцию пока она не выполнится без исключений
(но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено
исключение типа TooManyErrors
"""


class TooManyErrors(Exception):
    pass


def repeat(times):

    def func_decorator(func):

        def wrapper(args):
            nonlocal times
            try:
                if not times:
                    raise TooManyErrors
                print(f'Найти {args} число фибоначи')
                result = func(args)
                times -= 1
                print(f'Функцию можно выполнить еще {times} раз')
                return result
            except TooManyErrors:
                return f'TooManyErrors'

        return wrapper

    return func_decorator


@repeat(2)
def func(number):
    fib1 = 1
    fib2 = 1
    while number:
        number -= 1
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


print(func(5))
print(func(10))
print(func(20))
