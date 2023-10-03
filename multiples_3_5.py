# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python


def solution(number):
    if number < 0:
        return 0
    total = 0
    number -= 1
    while number > 0:
        if (number % 3 == 0) and (number % 5 == 0):
            total += number
            number -= 1
        elif (number % 3 == 0) or (number % 5 == 0):
            total += number
            number -= 1
        else:
            number -= 1
    return total
