"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets,
with values between 0 and 255, inclusive.
Input to the function is guaranteed to be a single string.

Решение проверенно на Codewars
"""


def is_valid_IP(str_):
    alf = 'qwertyuiopasdfghjklzxcvbnm'
    lst = str_.split('.')
    if len(lst) != 4:
        return False
    for i in lst:
        for j in i:
            if j in alf:
                return False
            if j == ' ':
                return False
        if int(i) < 0 or int(i) > 255:
            return False
        if i[0] == '0' and len(i) > 1:
            return False
    return True


if __name__ == '__main__':
    str_ = '123.045.067.089'
    print(is_valid_IP(str_))