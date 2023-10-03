# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

"""Valid pieces are as follows:
        Battleship (1): 4 cells
        Cruiser (2): 3 cells
        Destroyer (3): 2 cells
        Submarine (4): 1 cell

    All pieces must be present, no missing pieces or extra pieces are permitted
    All pieces must have one empty space between themselves and any other ships. No adjacent pieces allowed.
    Input is a 2d array.
    Function call: validate_battlefield(field)
    Returns True or False
    """
import numpy as np


def validate_battlefield(field):
    # Initialize coordinate counters
    x, y = 0, 0
    # Dictionary to store ship placement
    piece_dictionary = {1: 0,       # Battleship, size 4
                        2: 0,       # Cruiser, size 3
                        3: 0,       # Destroyer, size 2
                        4: 0}       # Submarine: size 1

    # Begin iterating
    pass


    












