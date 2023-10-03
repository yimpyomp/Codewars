# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python


def move_zeros(lst):
    filtered = [i for i in lst if i != 0]
    zero_list = [0 for i in range(lst.count(0))]
    return filtered + zero_list


move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
