# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
test_1 = "Hey fellow warriors"


def spin_words(sentence):
    sentence = list(sentence.split(' '))
    for i in range(len(sentence)):
        if len(sentence[i]) < 5:
            continue
        else:
            sentence[i] = sentence[i][::-1]
    return ' '.join(sentence)


print(spin_words(test_1))

