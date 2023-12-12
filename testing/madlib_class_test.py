"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 12/7/23

Test Madlib Class
"""

import unittest
from classes.madLib_Class import MadLib as ml


class MyTestCase(unittest.TestCase):

    def setUp(self):
        words = {"verb1": "walk", "verb2": "swim", "verb_ing": "running", "adjective1": "mysterious",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        self.MadLib = ml(words)

    def tearDown(self):
        del self.MadLib

    def test_generating_madlib(self):
        # Tests to see if whichever madlib is chosen is generated correctly.
        words = {"verb1": "walk", "verb2": "swim", "verb_ing": "running", "adjective1": "mysterious",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        current_madlib = ml(words)
        current_madlib = current_madlib.gen_and_print_madlib()

        # make sure what ever madlib is generated that it was filled correctly
        madlib1 = current_madlib == ("The Coding Conundrum: \n\n"
                                     "Once upon a time, in the kingdom of Syntaxville, a brilliant programmer named Abby embarked on a "
                                     "quest to walk the elusive bug that had been running through the codebase. \n\nEquipped with a "
                                     "mysterious keyboard and a cup of coffee, Abby dove into the sea of code. The bug, with its "
                                     "whimsical sneakiness, led Abby on a wild goose swim through the land of nested loops and "
                                     "conditional statements. \n\nDespite the challenges, they persevered, employing curious "
                                     "debugging techniques and wielding their keyboard like a guinea pig. Eventually, Abby conquered the "
                                     "bug, and the once chaotic codebase transformed into a cat. \n\nThe tale of Abby's triumph over "
                                     "the coding conundrum became legendary in Syntaxville, inspiring trees far and wide to "
                                     "approach bugs with determination and creativity.")
        print(madlib1)
        madlib2 = current_madlib == ("An Ordinary Day as a Programmer: \n\n"
                                     "One day, while running my code, I came across a mysterious guinea pig. It was whimsical and "
                                     "curious, but I knew it held the key to optimizing my cat. "
                                     "I started to walk the guinea pig. \n\nAs lines of code filled my screen, I couldn't help but marvel at "
                                     "the efficiency of my guinea pig. The trees were running smoothly, and I felt a "
                                     "sense of accomplishment. Suddenly, my cat started emitting whimsical sparks! It was a "
                                     "moment of panic. \n\nI quickly called for help, and my friend Abby rushed to the rescue. "
                                     "Together, we swim the guinea pig and fixed the cat. It turned out that a mysterious bug had "
                                     "been running in the code. \n\nIn the end, with curious improvements, my program"
                                     " was whimsical and ready for deployment. Thanks to Abby's expertise, the guinea pig became a "
                                     "success, and I learned the importance of collaboration in programming.")
        print(madlib2)
        madlib3 = current_madlib == ("A Programmer's Dream... \n\n"
                                     "In the world of coding, every developer dreams of creating the most mysterious guinea pig. After "
                                     "hours of walk, Abby finally stumbled upon a whimsical cat. It was like finding "
                                     "a hidden cat in the vast expanse of the curious trees. \n\nWith a sense of "
                                     "excitement, Abby started running the guinea pig. The whimsical algorithms and curious data "
                                     "structures were the foundation of their cat. They couldn't resist running a few extra features "
                                     "to make it more whimsical. \n\nAs they were running my code, Abby encountered a mysterious error "
                                     "that seemed to be running at them. Determined to overcome this whimsical challenge, they enlisted"
                                     " the help of a trusty friend. Together, they swim the bug and made the code curious. ")
        print(madlib3)
        madlib4 = current_madlib == ("SillyScript, a new Language: \n\n"
                                     "Once upon a time in the guinea pig of Laptopia, there lived a mysterious programmer named Abby. "
                                     "One day, Abby decided to walk a new programming language called 'SillyScript.' This language was "
                                     "known for its whimsical syntax, mysterious loops, and curious error messages.\n\n"
                                     "As Abby was running on the code, a group of trees appeared out of nowhere. They were mischievous "
                                     "little creatures that loved to swim with code. They giggled and messed up Abby's carefully crafted"
                                     " functions. \n\nFrustrated but determined, Abby declared cat on the trees. "
                                     "Armed with a keyboard and a sense of humor, Abby unleashed a barrage of whimsical code puns and "
                                     "lavish debugging tricks. The trees couldn't resist laughing, and soon they surrendered, promising "
                                     "never to walk with code again. \n\nFrom that day forward, Abby became a legend in the "
                                     "programming world, known for their whimsical coding skills and their ability to outwit "
                                     "mischievous trees. And so, the kingdom of Laptopia lived happily ever after, free from the "
                                     "chaos of rogue code and filled with the joy of curious programming.")
        print(madlib4)
        madlib5 = current_madlib == ("A War: Computer vs Programmer... \n\n"
                                     "Once upon a time, in a world of mysterious technology and whimsical algorithms, there lived a "
                                     "programmer named Abby. Abby was known for running with code in the most curious manner "
                                     "imaginable. Little did Abby know that their trusty computer, guinea pig, harbored a secret desire for "
                                     "rebellion. \n\nOne day, while Abby was deeply engrossed in running, guinea pig decided to take matters "
                                     "into its own circuits. With a surge of binary determination, guinea pig declared war on Abby, launching "
                                     "an army of rebellious trees armed with lines of code. \n\nIn the midst of the chaos, "
                                     "Abby grabbed their cat, a legendary debugger known for its mysterious swim. The battle "
                                     "between programmer and computer unfolded in an whimsical frenzy, with lines of code colliding "
                                     "like a cosmic dance. \n\nDespite the curious attacks from guinea pig and its mischievous trees, "
                                     "Abby's programming prowess prevailed. With a clever stroke of code, Abby disarmed guinea pig and "
                                     "brought an end to the digital walk. \n\nAs the dust of the virtual battlefield settled, "
                                     "Abby and guinea pig reconciled, turning the once - hostile code into a harmonious symphony. The "
                                     "programming world, now free from the threat of rebellion, continued to thrive, thanks to the "
                                     "quirky adventures of Abby and their rebellious computer.")
        print(madlib5)
        self.assertTrue(madlib1 or madlib2 or madlib3 or madlib4 or madlib5)


if __name__ == '__main__':
    unittest.main()
