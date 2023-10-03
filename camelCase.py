# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python


def to_camel_case(text):
    words = []
    for character in text:
        if character.isalpha():
            continue
        else:
            position = text.index(character)
            words.append(text[:position])
