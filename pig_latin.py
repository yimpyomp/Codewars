# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text):
    message = text.split(' ')
    translation = []
    for word in message:
        if not word.isalpha():
            translation.append(word)
        else:
            p = word[1:] + word[0] + 'ay'
            translation.append(p)
    return ' '.join(translation)

