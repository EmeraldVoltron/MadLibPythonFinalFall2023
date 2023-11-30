"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 11/30/2023

MadLib Class
"""

import random


class MadLib:
    # list of different madlib options:
    madlib1 = ""
    madlib2 = ""
    madlib3 = ""
    madlib4 = ""
    madlib5 = ""
    # madlib list
    madlibs_list = [madlib1, madlib2, madlib3, madlib4, madlib5]

    # madlib randomGenerator(chooses random mad lib from the 5 above
    currentMadLib = madlibs_list[random.randint(0, 4)]


    def __init__(self, words):
        self.words = words

        # inner function
        def generateMadLib(words):
            pass

        generateMadLib(self.words)

    def printMadLib(self):
        # returns a string of completed madlib
        pass







