"""
Abigail Boggs
amboggs@dmacc.edu
last edited: 12/7/23

Unit Testing for words inputs
"""

import unittest
import gui.madLib_gui

class MyTestCase(unittest.TestCase):
    def test_blank_verb1(self):
        words = {"verb1": " ", "verb2": "swim", "verb_ing": "running", "adjective1": "mysterious",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_blank_verb2(self):
        words = {"verb1": "run", "verb2": " ", "verb_ing": "running", "adjective1": "mysterious",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_blank_verbing(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": " ", "adjective1": "mysterious",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_blank_adj1(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": " ",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_blank_adj2(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": "mysterious",
                 "adjective2": " ", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_blank_adj3(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": "red",
                 "adjective2": "whimsical", "adjective3": " ", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_blank_noun1(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": "red",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": " ", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_blank_noun2(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": "red",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": " ",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_blank_pnoun(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": "red",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": " ", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_blank_name(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": "red",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": " "}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_invalid_verb1(self):
        words = {"verb1": "aaa", "verb2": "walk", "verb_ing": "dancing", "adjective1": "red",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_invalid_verb2(self):
        words = {"verb1": "run", "verb2": "aaa", "verb_ing": "dancing", "adjective1": "red",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_invalid_verbing(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "aaa", "adjective1": "red",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_invalid_adj1(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": "aaa",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_invalid_adj2(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": "red",
                 "adjective2": "aaa", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_invalid_adj3(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": "red",
                 "adjective2": "whimsical", "adjective3": "aaa", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_invalid_noun1(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": "red",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "aaa", "noun2": "cat",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_invalid_noun2(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": "red",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "aaa",
                 "p_noun": "trees", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)

    def test_invalid_pnoun(self):
        words = {"verb1": "run", "verb2": "walk", "verb_ing": "dancing", "adjective1": "red",
                 "adjective2": "whimsical", "adjective3": "curious", "noun1": "guinea pig", "noun2": "cat",
                 "p_noun": "aaa", "name": "Abby"}
        valid = gui.madLib_gui.test_words(words)
        self.assertFalse(valid)


if __name__ == '__main__':
    unittest.main()