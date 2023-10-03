# https://www.codewars.com/kata/59f7597716049833200001eb/train/python
# This the easy one ^^^^^^^^^
# https://www.codewars.com/kata/59f98052120be4abfa000304/train/python
# This the hard one ^^^^^^^^^


class Memoize:
    def __init__(self, function):
        self.function = function
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.function(*args)
        return self.cache[args]


# Easy version
flippas = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}


def solve(a, b):
    count = 0
    for i in range(a, b):
        try:
            flip = ''.join([flippas[char] for char in str(i)])
            print(flip, str(i))
            if flip[::-1] == str(i):
                count += 1
        except KeyError:
            continue
    return count


# Hard version
@Memoize
def upsidedown(x, y):
    count = 0
    for i in range(int(x), int(y) + 1):
        try:
            flip = ''.join([flippas[char] for char in str(i)])
            #print(flip, str(i))
            if flip[::-1] == str(i):
                count += 1
        except KeyError:
            continue
    end = time()
    return count, end

from time import time
start = time()
res, end = upsidedown('100000','12345678900000000')
print(res)
print(end - start)



