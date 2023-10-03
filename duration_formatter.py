# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
# Return combination of years, days, hours, minutes, and seconds
duration_factors = {'year': 3600 * 24 * 365, 'day': 3600 * 24, 'hour': 3600, 'minute': 60, 'second': 1}


def format_duration(seconds):
    if seconds == 0:
        return '0'
    conversions = []
    for label, factor in duration_factors.items():
        if seconds // factor:
            conversion = seconds // factor
            seconds -= conversion * factor
            if conversion > 1:
                conversions.append(f'{conversion} {label}s')
            else:
                conversions.append(f'{conversion} {label}')
        else:
            continue
    if len(conversions) == 1:
        return str(conversions[0])
    elif len(conversions) == 2:
        return f'{conversions[0]} and {conversions[1]}'
    else:
        return ', '.join(conversions[:-1]) + f' and {conversions[-1]}'


print(format_duration(0))