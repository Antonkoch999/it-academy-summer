def students(n):
    dct = {}
    for mi in range(1, n + 1):
        print('Введите количество языков:')
        count = int(input())
        lst = []
        for language in range(count):
            print('Введите иностранные языки:')
            lst.append(str(input()))
            dct[mi] = lst
    list_values = list(dct.values())
    common_list = 
    return dct


if __name__ == '__main__':
    n = 3
    print(students(n))
