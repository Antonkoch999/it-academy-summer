"""
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в
файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет
необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла
top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""


import re


def create_new_file():

    try:
        with open('ratings.list', 'r') as file:
            flag = False
            f = open('top250.txt', 'w')

            for line in file:

                if not flag:
                    if line == 'New  Distribution  Votes  Rank  Title\n':
                        flag = True
                        continue
                    else:
                        continue

                else:
                    if line == 'BOTTOM 10 MOVIES (1500+ VOTES)\n':
                        break
                    else:
                        f.write(line)
                        continue

    except FileNotFoundError:
        print('File not found')


def create_years_rating_name_file():

    with open('top250.txt', 'r') as top:
        file_years = open('years.txt', 'w')
        years = re.findall(r'\D\d{4}\D', top.read())
        for el in years:
            gistogram = f'>>>{"*" * (int(el[1:-1]) - 1895)}>>>{el[1:-1]}\n'
            file_years.write(str(gistogram))

    with open('top250.txt', 'r') as top:
        file_rating = open('rating.txt', 'w')
        rating = re.findall(r'\d\.\d', top.read())
        for el in rating:
            gistogram = f'>>>{"*" * int(float(el) * 10)} >>> {el}\n'
            file_rating.write(str(gistogram))

    with open('top250.txt', 'r') as top:
        file_name = open('top250_movies.txt', 'w')
        name = re.findall(r'[A-Za-z]+\d[A-Za-z]+|[A-Za-z]+\D+[A-Za-z]+|[A-Za-z]+\s', top.read())
        for el in name:
            movie = f'Movie title: {el}\n'
            file_name.write(str(movie))


create_new_file()
create_years_rating_name_file()
