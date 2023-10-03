# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python


def strip_comments(strng, markers):
    split_string = strng.splitlines()
    for index, line in enumerate(split_string):
        for marker in markers:
            if marker in line:
                demarcation = line.index(marker)
                split_string[index] = (line[:demarcation]).rstrip()
    return '\n'.join(split_string)




test_string = 'apples, pears # and bananas\ngrapes\nbananas #!apples'
print(strip_comments(test_string, ['#', '!']))