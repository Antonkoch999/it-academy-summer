"""
Оформите решение задач из прошлых домашних
работ в функции. Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только
функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все
переданные функции
"""


from src.func import funcs


def runner(*args):
    lst_method = [el for el in dir(funcs) if '__' not in el]

    def get_func(arg):
        for el in arg:
            print(f'Result function {el}:{getattr(funcs, el)()}')

    if not args:
        return get_func(lst_method)
    else:
        return get_func(args)


runner()
runner('binary')
runner('pair_el', 'binary')
