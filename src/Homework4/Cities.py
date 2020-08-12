"""
Дан список стран и городов каждой страны.
Затем даны названия городов. Для каждого города укажите,
в какой стране он находится.
"""


import random


def cities(number_country, number_cities):
    dct = {}
    lst = []
    result = []

    for line in range(number_country):
        country_, *city = input('Введите страну и города:').split()
        dct[country_] = list(city)

    for i in range(number_cities):
        lst.append(random.choice(random.choice(list(dct.values()))))
    print(lst)
    for city in lst:
        for key, value in dct.items():
            if city in value:
                result.append(key)

    return result


if __name__ == '__main__':
    number_country, number_cities = 2, 3
    print(cities(number_country, number_cities))
