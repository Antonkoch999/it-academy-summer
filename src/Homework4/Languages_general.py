"""
Языки
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
"""


def students(student):
    dct = {}

    for mi in range(1, student + 1):
        count = int(input('Введите количество языков:'))
        lst = []
        for language in range(count):
            lst.append(str(input('Введите иностранные языки:')))
            dct[mi] = lst

    all_know = set()
    for value in dct.values():
        all_know.update(value)

    sets = []
    for value in dct.values():
        sets.append(set(value))
    one_know = list(set.intersection(*map(set, sets)))

    return 'Кол-во языков которые знают все школьники: {}\n' \
           'Список этих языков: {}\n' \
           'Кол-во языков которые знает хотя бы один школьник: {}\n' \
           'Список этих языков: {}\n'.format(one_know,
                                             len(one_know),
                                             all_know,
                                             len(all_know))


if __name__ == '__main__':
    student = int(input('Введите количество школьников:'))
    print(students(student))
