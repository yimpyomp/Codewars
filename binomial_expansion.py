# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b/train/python
from math import factorial


def expand(expr):
    carrot_index = expr.find('^')
    degree = int(expr[carrot_index + 1:])
    if degree == 0:
        return str(1)
    if degree == 1:
        return expr[1: carrot_index - 1]
    coefficient, variable_index, constant = None, None, None
    for character in expr:
        if character.isalpha():
            variable_index = expr.index(character)
            break
    variable = expr[variable_index]
    if variable_index == 1:
        coefficient = 1
    if expr[variable_index - 1] == '-':
        coefficient = -1
    if not coefficient:
        coefficient = int(expr[1: variable_index])
    close_index = expr.find(')')
    if expr[variable_index + 1] == '+':
        constant = int(expr[variable_index + 2: close_index])
    else:
        constant = int(expr[variable_index + 1: close_index])

    k = 1
    terms = []
    if (coefficient == 1) or (coefficient == -1) and (degree % 2 == 0):
        terms.append(f'{variable}^{degree}')
    elif (coefficient == -1) and (degree % 2 != 0):
        terms.append(f'-{variable}^{degree}')
    else:
        terms.append(f'{int(coefficient ** degree)}{variable}^{degree}')

    while degree - k > 0:

        n_pick = factorial(degree) / (factorial(k) * factorial(degree - k))
        next_coefficient = n_pick * (coefficient ** (degree - k)) * (constant ** k)
        if next_coefficient > 0:
            next_coefficient = f'+{int(next_coefficient)}'
        else:
            next_coefficient = f'{int(next_coefficient)}'
        if degree - k == 1:
            terms.append(f'{next_coefficient}{variable}')
        else:
            terms.append(f'{next_coefficient}{variable}^{degree - k}')
        k += 1
    if (constant ** degree) > 0:
        terms.append(f'+{int(constant ** degree)}')
    else:
        terms.append(f'{int(constant ** degree)}')

    return ''.join(terms)
