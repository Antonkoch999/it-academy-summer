"""
John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;
Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
Could you make a program that
1. makes this string uppercase
2. gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name.
Last name and first name of a guest come in the result
between parentheses separated by a comma.

So the result of function meeting(s) will be:
"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)
(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(
TORNBULL, BJON)"
It can happen that in two distinct families with the same
family name two people have the same first name too.

Codewars lvl 6
"""


def meeting(s):
    lst = s.split(';')
    new_lst = []
    for el in lst:
        for letter in el:
            index_ = el.index(letter)
            if letter == ':':
                name = '(' + el[index_ + 1:] + ', ' + el[:index_] + ')'
                new_lst.append(name.upper())
                break
    lst1 = sorted(new_lst)
    return ''.join(lst1)


if __name__ == '__main__':
    s = "Alex:Arno;Alissa:Cornwell;Sarah:Bell;Andrew:" \
        "Dorries;Ann:Kern;Haley:Arno;Paul:Dorny;Madison:Kern"
    print(meeting(s))
