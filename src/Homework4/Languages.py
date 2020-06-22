# def name(func):
#     def wrapper(*args, **kwargs):
#
#         res = func(*args, **kwargs)
#
#         return res
#     return wrapper


def students(n, m1, m2, m3):
    # dct = {}
    lst1 = []
    lst2 = []
    lst3 = []
    count = 0
    count_lst = []
    lang_lst = []
    for languages in range(m1):
        lst1.append(str(input()))
        # dct[1] = lst1
    for languages in range(m2):
        lst2.append(str(input()))
        # dct[2] = lst2
    for languages in range(m3):
        lst3.append(str(input()))
        # dct[3] = lst3
    lst = lst1 + lst2 + lst3
    for item in lst:
        if item in lst1 and item in lst2 and item in lst3:
            count += 1
            count_lst.append(item)
        if item in lst1 or item in lst2 or item in lst3:
            lang_lst.append(item)
    st = set(lang_lst)
    lang_lst = list(st)
    return count, count_lst, len(st), lang_lst


if __name__ == '__main__':
    n, m1, m2, m3 = 3, 2, 3, 3
    print(students(n, m1, m2, m3))

