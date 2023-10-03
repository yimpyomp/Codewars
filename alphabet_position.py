# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def alphabet_position(text):
    result = [str(1 + alphabet.index(i.lower())) for i in text if i.isalpha()]
    return ' '.join(result)