"""
Move the first letter of each word to the end of it,
then add "ay" to the end of the word.
Leave punctuation marks untouched.
Examples:

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

Codewars(lvl5)
"""


def pig_it(text):
    import string
    punct = string.punctuation
    lst = text.split(' ')
    lst1 = []
    for word in lst:
        if word in punct:
            lst1.append(word)
            continue
        word = word[1:] + word[0] + 'ay'
        lst1.append(word)
    final = ' '.join(lst1)
    return final


if __name__ == '__main__':
    text = 'O tempora o mores !'
    print(pig_it(text))
