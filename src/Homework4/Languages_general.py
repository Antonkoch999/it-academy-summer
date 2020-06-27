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

    list_values = list(dct.values())
    all_language = []
    for el in list_values:
        for lang in el:
            if lang in all_language:
                continue
            else:
                all_language.append(lang)

    all_know = []
    all_know_number = 0
    for elem in all_language:
        for key, value in dct.items():
            if elem not in value:
                break
            elif elem in all_know:
                continue
            else:
                all_know_number += 1
                all_know.append(elem)

    one_know = []
    one_know_number = 0
    for elem in all_language:
        for key, value in dct.items():
            if elem in one_know:
                continue
            elif elem in value:
                one_know_number += 1
                one_know.append(elem)

    return 'Кол-во языков которые знают все школьники: {}\n' \
           'Список этих языков: {}\n' \
           'Кол-во языков которые знает хотя бы один школьник: {}\n' \
           'Список этих языков: {}\n'.format(all_know_number, all_know,
                                             one_know_number, one_know)


if __name__ == '__main__':
    student = 3
    print(students(student))
