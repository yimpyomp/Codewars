# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python

decimal_to_roman = {4000: 'MMMM', 3000: 'MMM', 2000: 'MM', 1000: 'M', 900: 'CM',  800: 'DCCC', 700: 'DCC', 600: 'DC',
                    500: 'D', 400: 'CD', 300: 'CCC', 200: 'CC', 100: 'C', 90: 'XC', 80: 'LXXX', 70: 'LXX', 60: 'LX',
                    50: 'L', 40: 'XL', 30: 'XXX', 20: 'XX', 10: 'X', 9: 'IX', 8: 'VIII', 7: 'VII', 6: 'VI', 5: 'V',
                    4: 'IV', 3: 'III', 2: 'II', 1: 'I'}
roman_to_decimal = {'MMMM': 4000, 'MMM': 3000, 'MM': 2000, 'M': 1000, 'CM': 900, 'DCCC': 800, 'DCC': 700, 'DC': 600,
                    'D': 500, 'CD': 400, 'CCC': 300, 'CC': 200, 'C': 100, 'XC': 90, 'LXXX': 80, 'LXX': 70, 'LX': 60,
                    'L': 50, 'XL': 40, 'XXX': 30,'XX': 20, 'X': 10, 'IX': 9, 'VIII': 8, 'VII': 7, 'VI': 6,  'V': 5,
                    'IV': 4, 'III': 3, 'II': 2, 'I': 1}
decimal_list = [1000, 100, 10, 1]


class RomanNumerals:
    @staticmethod
    def to_roman(val):
        romanized = []
        for entry in decimal_list:
            if val // entry >= 1:
                quantity = val // entry
                romanized.append(decimal_to_roman[quantity * entry])
                val = val % entry
        return ''.join(romanized)

# You know what you did
    @staticmethod
    def from_roman(roman_num):
        decimal_sum = 0
        i = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num):
                if roman_to_decimal[roman_num[i]] >= roman_to_decimal[roman_num[i + 1]]:
                    decimal_sum += roman_to_decimal[roman_num[i]]
                    i += 1
                else:
                    next_val = roman_to_decimal[roman_num[i + 1]] - roman_to_decimal[roman_num[i]]
                    decimal_sum += next_val
                    i += 2
            else:
                decimal_sum += roman_to_decimal[roman_num[i]]
                i += 1
        return decimal_sum


print(RomanNumerals().from_roman('MMMCMLXXVIII'))














