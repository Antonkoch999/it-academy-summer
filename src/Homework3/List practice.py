"""
1. Используйте генератор списков чтобы получить
      следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить
   следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить
   следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы
   в исходном списке этого элемента не было.
"""


def list_practice(str1, str2):
    str_lst = [i + j for i in str1 for j in str2]
    print(str_lst)
    str_lst1 = str_lst[::2]
    print(str_lst1)
    int_lst = [str(i) + 'a' for i in range(1, 5)]
    el = int_lst.pop(1)
    print(el)
    print(int_lst)
    int_lst1 = int_lst[:]
    int_lst1.append(el)
    return int_lst1


if __name__ == '__main__':
    str1 = 'ab'
    str2 = 'bcd'
    print(list_practice(str1, str2))
