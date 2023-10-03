# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python


def make_readable(seconds):
    time_list = []
    if seconds // 3600:
        hours = seconds // 3600
        seconds = seconds - (hours * 3600)
        time_list.append(str(hours).zfill(2))
    else:
        time_list.append('00')

    if seconds // 60:
        minutes = seconds // 60
        seconds = seconds - (minutes * 60)
        time_list.append(str(minutes).zfill(2))
    else:
        time_list.append('00')

    if seconds:
        time_list.append(str(seconds).zfill(2))
    else:
        time_list.append('00')

    return ':'.join(time_list)


