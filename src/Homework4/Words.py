"""
Слова
Во входной строке записан текст.
Словом считается последовательность непробельных символов
идущих подряд, слова разделены одним или большим числом
пробелов или символами конца строки. Определите,
сколько различных слов содержится в этом тексте.
"""


def words(str_):
    str_.splitlines()
    str1 = ''.join(str_)
    lst = str1.split()
    return len(set(lst))


if __name__ == '__main__':
    str_ = 'asdwdw, asdwdw, asdwdw, asdwdw. asdwdw:  asdwqdqw  b\n    m  asdawdaw a ddasdac  d\n'
    print(words(str_))
