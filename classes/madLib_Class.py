"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 12/7/23

MadLib Class
"""

import random
import re


class MadLib:

    def __init__(self, words):
        self.words = words

    def gen_and_print_madlib(self):
        # strings of different madlib options:
        madlib1 = ("The Coding Conundrum: \n\n"
                   "Once upon a time, in the kingdom of Syntaxville, a brilliant programmer named NAME embarked on a "
                   "quest to VERB1 the elusive bug that had been VERBING through the codebase. \n\nEquipped with a "
                   "ADJECTIVE1 keyboard and a cup of coffee, NAME dove into the sea of code. The bug, with its "
                   "ADJECTIVE2 sneakiness, led NAME on a wild goose VERB2 through the land of nested loops and "
                   "conditional statements. \n\nDespite the challenges, they persevered, employing ADJECTIVE3 "
                   "debugging techniques and wielding their keyboard like a NOUN1. Eventually, NAME conquered the "
                   "bug, and the once chaotic codebase transformed into a NOUN2. \n\nThe tale of NAME's triumph over "
                   "the coding conundrum became legendary in Syntaxville, inspiring PNOUN far and wide to "
                   "approach bugs with determination and creativity.")
        madlib2 = ("An Ordinary Day as a Programmer: \n\n"
                   "One day, while VERBING my code, I came across a ADJECTIVE1 NOUN1. It was ADJECTIVE2 and "
                   "ADJECTIVE3, but I knew it held the key to optimizing my NOUN2. "
                   "I started to VERB1 the NOUN1. \n\nAs lines of code filled my screen, I couldn't help but marvel at "
                   "the efficiency of my NOUN1. The PNOUN were running smoothly, and I felt a "
                   "sense of accomplishment. Suddenly, my NOUN2 started emitting ADJECTIVE2 sparks! It was a "
                   "moment of panic. \n\nI quickly called for help, and my friend NAME rushed to the rescue. "
                   "Together, we VERB2 the NOUN1 and fixed the NOUN2. It turned out that a ADJECTIVE1 bug had "
                   "been VERBING in the code. \n\nIn the end, with ADJECTIVE3 improvements, my program"
                   " was ADJECTIVE2 and ready for deployment. Thanks to NAME's expertise, the NOUN1 became a "
                   "success, and I learned the importance of collaboration in programming.")
        madlib3 = ("A Programmer's Dream... \n\n"
                   "In the world of coding, every developer dreams of creating the most ADJECTIVE1 NOUN1. After "
                   "hours of VERB1, NAME finally stumbled upon a ADJECTIVE2 NOUN2. It was like finding "
                   "a hidden NOUN2 in the vast expanse of the ADJECTIVE3 PNOUN. \n\nWith a sense of "
                   "excitement, NAME started VERBING the NOUN1. The ADJECTIVE2 algorithms and ADJECTIVE3 data "
                   "structures were the foundation of their NOUN2. They couldn't resist VERBING a few extra features "
                   "to make it more ADJECTIVE2. \n\nAs they were VERBING my code, NAME encountered a ADJECTIVE1 error "
                   "that seemed to be VERBING at them. Determined to overcome this ADJECTIVE2 challenge, they enlisted"
                   " the help of a trusty friend. Together, they VERB2 the bug and made the code ADJECTIVE3. ")
        madlib4 = ("SillyScript, a new Language: \n\n"
                   "Once upon a time in the NOUN1 of Laptopia, there lived a ADJECTIVE1 programmer named NAME. "
                   "One day, NAME decided to VERB1 a new programming language called 'SillyScript.' This language was "
                   "known for its ADJECTIVE2 syntax, ADJECTIVE1 loops, and ADJECTIVE3 error messages.\n\n"
                   "As NAME was VERBING on the code, a group of PNOUN appeared out of nowhere. They were mischievous "
                   "little creatures that loved to VERB2 with code. They giggled and messed up NAME's carefully crafted"
                   " functions. \n\nFrustrated but determined, NAME declared NOUN2 on the PNOUN. "
                   "Armed with a keyboard and a sense of humor, NAME unleashed a barrage of ADJECTIVE2 code puns and "
                   "lavish debugging tricks. The PNOUN couldn't resist laughing, and soon they surrendered, promising "
                   "never to VERB1 with code again. \n\nFrom that day forward, NAME became a legend in the "
                   "programming world, known for their ADJECTIVE2 coding skills and their ability to outwit "
                   "mischievous PNOUN. And so, the kingdom of Laptopia lived happily ever after, free from the "
                   "chaos of rogue code and filled with the joy of ADJECTIVE3 programming.")
        madlib5 = ("A War: Computer vs Programmer... \n\n"
                   "Once upon a time, in a world of ADJECTIVE1 technology and ADJECTIVE2 algorithms, there lived a "
                   "programmer named NAME. NAME was known for VERBING with code in the most ADJECTIVE3 manner "
                   "imaginable. Little did NAME know that their trusty computer, NOUN1, harbored a secret desire for "
                   "rebellion. \n\nOne day, while NAME was deeply engrossed in VERBING, NOUN1 decided to take matters "
                   "into its own circuits. With a surge of binary determination, NOUN1 declared war on NAME, launching "
                   "an army of rebellious PNOUN armed with lines of code. \n\nIn the midst of the chaos, "
                   "NAME grabbed their NOUN2, a legendary debugger known for its ADJECTIVE1 VERB2. The battle "
                   "between programmer and computer unfolded in an ADJECTIVE2 frenzy, with lines of code colliding "
                   "like a cosmic dance. \n\nDespite the ADJECTIVE3 attacks from NOUN1 and its mischievous PNOUN, "
                   "NAME's programming prowess prevailed. With a clever stroke of code, NAME disarmed NOUN1 and "
                   "brought an end to the digital VERB1. \n\nAs the dust of the virtual battlefield settled, "
                   "NAME and NOUN1 reconciled, turning the once - hostile code into a harmonious symphony. The "
                   "programming world, now free from the threat of rebellion, continued to thrive, thanks to the "
                   "quirky adventures of NAME and their rebellious computer.")
        # list of all madlibs
        madlib_list = [madlib1, madlib2, madlib3, madlib4, madlib5]
        # madlib randomGenerator(chooses random mad lib from the 5 above
        # current_madlib = madlib1
        current_madlib = madlib_list[random.randint(0, len(madlib_list)-1)]
        # sets the title of the madlib, aka the first string in the madlib array
        words_dict = self.words

        # generates madlib
        # inner function
        def gen_madlib():
            # Regex to replace words in the strings
            madlib = re.sub("NAME", words_dict["name"], current_madlib)
            madlib = re.sub("VERB1", words_dict["verb1"], madlib)
            madlib = re.sub("VERB2", words_dict["verb2"], madlib)
            madlib = re.sub("VERBING", words_dict["verb_ing"], madlib)
            madlib = re.sub("ADJECTIVE1", words_dict["adjective1"], madlib)
            madlib = re.sub("ADJECTIVE2", words_dict["adjective2"], madlib)
            madlib = re.sub("ADJECTIVE3", words_dict["adjective3"], madlib)
            madlib = re.sub("NOUN1", words_dict["noun1"], madlib)
            madlib = re.sub("NOUN2", words_dict["noun2"], madlib)
            madlib = re.sub("PNOUN", words_dict["p_noun"], madlib)
            # return the completed madlib
            return madlib

        # generate madlib
        created_madlib = gen_madlib()
        # returns a string of completed madlib
        return created_madlib
