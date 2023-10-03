# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python

def count_smileys(arr):
    eyes = [':', ';']
    nose = ['-', '~']
    mouf = [')', 'D']
    faces = 0
    for item in arr:
        if len(item) < 2:
            faces += 0
        else:
            if len(item) == 2:
                if (item[0] in eyes) and (item[1] in mouf):
                    faces += 1
                else:
                    faces += 0
            elif len(item) == 3:
                if (item[0] in eyes) and (item[1] in nose) and (item[2] in mouf):
                    faces += 1
                else:
                    faces += 0
    return faces
