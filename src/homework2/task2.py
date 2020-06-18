"""Найти самое длинное слово в введенном предложении. В случае если их
    несколько, самое левое в строке Учтите что в предложении есть знаки
    препинания.
"""


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """

    # write your code here
    import string
    punct = string.punctuation + ' '
    for el in punct:
        str_ = str_.replace(str(el), ',')
    lisst = str_.split(',')
    index = 0
    for i in range(1, len(lisst)):
        if len(lisst[index]) < len(lisst[i]):
            index = i
    return 'Самое длинное слово:', lisst[index]  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = 'word            wordd'
    print(longest_word(str_))
