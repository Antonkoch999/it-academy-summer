"""
The new "Avengers" movie has just been released!
There are a lot of people at the cinema box
office standing in a huge line. Each of them
has a single 100, 50 or 25 dollar bill.
An "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk.
He wants to sell a ticket to every
single person in this line.
Can Vasya sell a ticket to every person and
give change if he initially has no money and
sells the tickets strictly
in the order people queue?
Return YES, if Vasya can sell a ticket to
every person and give change with the bills
he has at hand at that moment. Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES
tickets([25, 100]) # => NO. Vasya will not have
enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya
will not have the right bills to give 75
dollars of change (you can't make two bills
of 25 from one of 50)

Codewars lvl 6
"""


def tickets(people_lst):
    counter_two_five = 0
    counter_fifty = 0
    for el in people_lst:
        if el == 25:
            counter_two_five += 1
            continue
        if el == 50:
            if counter_two_five <= 0:
                return 'NO'
            counter_fifty += 1
            counter_two_five -= 1
        if el == 100:
            if counter_fifty <= 0 and counter_two_five >= 3:
                counter_two_five -= 3
                continue
            if (counter_two_five <= 0 and counter_fifty >= 0) or \
                    (counter_two_five >= 0 and counter_fifty <= 0):
                return 'NO'
            counter_two_five -= 1
            counter_fifty -= 1
    return 'YES'


if __name__ == '__main__':
    people_lst = [25, 25, 25, 25, 25, 100, 50]
    print(tickets(people_lst))























