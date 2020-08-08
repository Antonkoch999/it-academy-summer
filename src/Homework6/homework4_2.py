"""
Дан список стран и городов каждой страны.
Затем даны названия городов. Для каждого города укажите,
в какой стране он находится.
"""

import collections


def cities(args):
    all_values = []
    result = []
    dct = {}
    with open('C:/Users/37533/it-academy-summer/src/country.txt', 'r') as \
            country:
        for line in country:
            country_, *city = line.split()
            dct[country_] = list(city)

    for key, value in dct.items():
        all_values.extend(value)
    repeat_cities = [key for key, value in  # Список повторяющихся городов
                     collections.Counter(all_values).items()
                     if value > 1]

    for city in args:
        if city in repeat_cities:
            for key, value in dct.items():
                if city in value:
                    result.append(f'{city} - {key}')
                continue
        else:
            for key, value in dct.items():
                if city in value:
                    result.append(f'{city} - {key}')

    return result


if __name__ == '__main__':
    print(cities(('Moscow',)))
