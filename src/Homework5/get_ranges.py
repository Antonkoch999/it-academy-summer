"""
Реализовать функцию get_ranges которая получает на
вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список
“сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst):
    new_lst = []

    for el in lst:
        if el == lst[0]:
            new_lst.append(str(el))
            if lst[0] + 1 == lst[1]:
                new_lst.append('-')
                break
            elif lst[0] + 1 != lst[1]:
                new_lst.append(',')
                break
            else:
                break

    for el in range(1, (len(lst) - 1)):
        if lst[el] - 1 == lst[el - 1] and lst[el] + 1 == lst[el + 1]:
            continue

        if lst[el] - 1 == lst[el - 1] and lst[el] + 1 != lst[el + 1]:
            new_lst.append(str(lst[el]))
            new_lst.append(',')
            continue

        if lst[el] + 1 == lst[el + 1] and lst[el] - 1 != lst[el - 1]:
            new_lst.append(str(lst[el]))
            new_lst.append('-')
            continue

        if lst[el] - 1 != lst[el - 1] and lst[el] + 1 != lst[el + 1]:
            new_lst.append(str(lst[el]))
            new_lst.append(',')
            continue

    new_lst.append(str(lst[-1]))
    str_ = ''.join(new_lst)
    return str_


if __name__ == '__main__':
    lst = [0, 1, 3, 4, 5, 6, 10, 12, 15, 16]
    print(get_ranges(lst))
