"""
Дан список. Выведите те его элементы,
которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
"""


def unique_el(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


if __name__ == '__main__':
    lst = [1,2,5,3,7,2,5,9,11]
    print(unique_el(lst))
