# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

# I hate when they have these generic ass function names
def solution(args):
    for i in range(1, len(args)):
        if args[i - 1] >= args[i]:
            args[i - 1], args[i] = args[i], args[i - 1]
    formatted = [args[0]]
    for i in range(1, len(args)):
        if formatted[-1] == args[i] + 1:
            continue
        else:
            pass

    return None
