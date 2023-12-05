"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 11/30/2023

MadLib Class
"""

import random


class MadLib:

    def __init__(self, words):
        self.words = words

    def gen_and_print_madlib(self):
        # list of different madlib options:
        madlib1 = []
        madlib2 = []
        madlib3 = []
        madlib4 = []
        madlib5 = []
        # madlib list
        madlibs_list = [madlib1, madlib2, madlib3, madlib4, madlib5]
        # madlib randomGenerator(chooses random mad lib from the 5 above

        currentMadLib = madlibs_list[random.randint(0, 4)]

        # generates madlib
        # inner function
        def gen_madlib():
            # generate madlib
            c_madlib = "Testing"
            return c_madlib

        #generate madlib
        created_madlib = gen_madlib()
        # returns a string of completed madlib
        return created_madlib






