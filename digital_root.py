# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    digi_sum = sum(int(i) for i in str(n))
    if digi_sum <= 9:
        return digi_sum
    else:
        while digi_sum > 9:
            n = digi_sum
            digi_sum = sum(int(i) for i in str(n))
        return digi_sum


print(digital_root(942))