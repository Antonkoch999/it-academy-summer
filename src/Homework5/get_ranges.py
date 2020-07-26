"""
Реализовать функцию get_ranges которая получает на
вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список
“сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges_v_2(lst):
    new_lst = []
    range_ = False
    rating_list = ''

    for el in lst:
        index_ = lst.index(el)

        if not range_:
            if el == lst[-1] or lst[index_ + 1] - el != 1:
                new_lst.append(str(el))
            else:
                rating_list += f'{str(el)}-'
                range_ = True

        else:
            if el == lst[-1] or lst[index_ + 1] - el != 1:
                rating_list += str(el)
                new_lst.append(rating_list)
                rating_list = ''
                range_ = False

    str_ = ', '.join(new_lst)
    return str_


if __name__ == '__main__':
    lst = [0, 1, 3, 5, 6, 7, 10, 12, 15, 16]
    print(get_ranges_v_2(lst))
