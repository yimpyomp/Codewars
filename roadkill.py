# https://www.codewars.com/kata/58e18c5434a3022d270000f2/train/python

ANIMALS = ['aardvark', 'alligator', 'armadillo', 'antelope', 'baboon', 'bear', 'bobcat', 'butterfly', 'cat', 'camel',
           'cow', 'chameleon', 'dog', 'dolphin', 'duck', 'dragonfly', 'eagle', 'elephant', 'emu', 'echidna', 'fish',
           'frog', 'flamingo', 'fox', 'goat', 'giraffe', 'gibbon', 'gecko', 'hyena', 'hippopotamus', 'horse', 'hamster',
           'insect', 'impala', 'iguana', 'ibis', 'jackal', 'jaguar', 'jellyfish', 'kangaroo', 'kiwi', 'koala',
           'killerwhale', 'lemur', 'leopard', 'llama', 'lion', 'monkey', 'mouse', 'moose', 'meercat', 'numbat', 'newt',
           'ostrich', 'otter', 'octopus', 'orangutan', 'penguin', 'panther', 'parrot', 'pig', 'quail', 'quokka',
           'quoll', 'rat', 'rhinoceros', 'racoon', 'reindeer', 'rabbit', 'snake', 'squirrel', 'sheep', 'seal', 'turtle',
           'tiger', 'turkey', 'tapir', 'unicorn', 'vampirebat', 'vulture', 'wombat', 'walrus', 'wildebeast', 'wallaby',
           'yak', 'zebra']
test_skid = "==========h===yyyyyy===eeee=n==a========"
skid_bear = '=====r=rrr=rra=====eee======bb====b======='
penguin = '======pe====nnnnnn=======================n=n=ng====u==iiii=iii==nn========================n='


def letter_search(data, test):
    for entry in data:
        skip_flag = False
        skip_count = 0
        if len(entry) >= len(test):
            for character in test:
                if character in entry:
                    continue
                else:
                    skip_flag = True
                    skip_count += 1
            if not skip_flag:
                if skip_flag <= 2:
                    return entry
        elif len(entry) < len(test):
            for character in entry:
                if character in test:
                    continue
                else:
                    skip_flag = True
                    if skip_flag <= 2:
                        return entry
            if not skip_flag:
                return entry
    return '??'


def road_kill(photo):
    match = ''.join([i for i in photo if i.isalpha()])
    flipped = match[::-1]
    if match in ANIMALS:
        return match
    if flipped in ANIMALS:
        return flipped
    else:
        final = letter_search(ANIMALS, photo)
    return final

