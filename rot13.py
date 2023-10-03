# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def rot13(message):
    ciphered = []
    for character in message:
        # Determine if character is a valid letter, take index if true
        if not character.isalpha():
            ciphered.append(character)
            continue

        else:
            current_index = alphabet.index(character.lower())
            shifted_index = current_index + 13
            # Adjust index if shift is out of range of alphabet
            if shifted_index > 25:
                shifted_index -= 26
        # Adjust for case
        if character.isupper():
            ciphered.append(alphabet[shifted_index].upper())
        else:
            ciphered.append(alphabet[shifted_index])

    return ''.join(ciphered)

