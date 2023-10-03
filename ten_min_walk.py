# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python


def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    x, y = 0, 0
    for item in walk:
        if item == 'n':
            y += 1
        if item == 's':
            y -= 1
        if item == 'e':
            x += 1
        if item == 'w':
            x -= 1

    if x == y == 0:
        return True
    else:
        return False


