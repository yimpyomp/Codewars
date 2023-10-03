# https://www.codewars.com/kata/54cf7f926b85dcc4e2000d9d/train/python


def frequencies(s):
    char_freq = {}
    if len(s) <= 1:
        return None
    for character in s:
        if character.lower() not in char_freq.keys():
            char_freq[character.lower()] = 1
        else:
            char_freq[character.lower()] += 1
    
