"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 11/30/23

MadLib Final Project, gui
"""
import csv
import tkinter
import tkinter as tk
from tkinter import messagebox
from classes import madLib_Class as ml


'''
Define functions/methods below here
'''


def start_madlib():
    """
    Start madlib
    """
    print("Starting Game")
    # activate all fields
    enable_text_fields()
    # clear all fields
    clear_text_fields()
    # activate create madlib button
    create_madlib_button["state"] = "normal"
    # deactivate start game button
    start_button["state"] = "disabled"


def add_words_to_dict():
    """
    Adds word to dictionary based on input fields
    :return: returns the words_dict now filled
    """
    print("Adding words to dictionary")
    # Add all words to dictionary
    empty_words_dict = {"verb1": "", "verb2": "", "verb_ing": "", "adjective1": "", "adjective2": "", "adjective3": "",
                        "noun1": "", "noun2": "", "p_noun": "", "name": ""}
    print(empty_words_dict)
    empty_words_dict.update({"verb1": str(verb_text_1.get(1.0, "end-1c"))})
    empty_words_dict.update({"verb2": str(verb_text_2.get(1.0, "end-1c"))})
    empty_words_dict.update({"verb_ing": str(verb_text_3.get(1.0, "end-1c"))})
    empty_words_dict.update({"adjective1": str(adjective_text_1.get(1.0, "end-1c"))})
    empty_words_dict.update({"adjective2": str(adjective_text_2.get(1.0, "end-1c"))})
    empty_words_dict.update({"adjective3": str(adjective_text_3.get(1.0, "end-1c"))})
    empty_words_dict.update({"noun1": str(noun_text_1.get(1.0, "end-1c"))})
    empty_words_dict.update({"noun2": str(noun_text_2.get(1.0, "end-1c"))})
    empty_words_dict.update({"p_noun": str(plural_noun_text_1.get(1.0, "end-1c"))})
    empty_words_dict.update({"name": str(name_text.get(1.0, "end-1c"))})
    print(empty_words_dict)
    return empty_words_dict


def test_words(words_dict):
    """
    Test all the words
    :param words_dict: test this dict
    :return: true or false if words are good or not
    """
    print("Testing words")
    words_pass_tf = False
    verb_rows = []
    verb_ing_rows = []
    adjective_rows = []
    noun_rows = []
    plural_noun_rows = []
    error_words = []
    try:
        # import verbs from csv file
        with open("../words/verbs.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                verb_rows.append(row[0])
            csvfile.close()

        # import ing verbs from csv file
        with open("../words/verbs-ing.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                verb_ing_rows.append(row[0])
            csvfile.close()

        # import adjectives from csv file
        with open("../words/adjectives.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                adjective_rows.append(row[0])
            csvfile.close()

        # import nouns from csv file
        with open("../words/nouns.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                noun_rows.append(row[0])
            csvfile.close()

        # import plural nouns from csv file
        with open("../words/plural-nouns.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                plural_noun_rows.append(row[0])
            csvfile.close()
    except IOError:
        print("Error could not read file.")

    # print(verb_rows)
    # print(verb_ing_rows)
    # TO-DO test all inputs before moving on
    try:
        verb1_test = False
        verb2_test = False
        verb_ing_test = False
        adjective1_test = False
        adjective2_test = False
        adjective3_test = False
        noun1_test = False
        noun2_test = False
        p_noun_test = False
        name_test = False
        for k, v in words_dict.items():
            # print(k)
            # print(v)
            v = str(v).lower()
            match k:
                case "verb_ing":
                    if v == " " or v == "":
                        verb_ing_test = False
                        error_words.append("Verb ending in -ing: cannot be blank")
                    else:
                        for verb in verb_ing_rows:
                            # debug print(str(v) + " : " + str(verb))
                            if v.lower() == verb.lower():
                                verb_ing_test = True
                        if verb_ing_test is not True:
                            error_words.append("Verb ending in -ing :" + str(v))
                case "verb1" | "verb2":
                    if v == " " or v == "":
                        if k == "verb1":
                            verb1_test = False
                            error_words.append("Verb 1: cannot be blank")
                        elif k == "verb2":
                            verb2_test = False
                            error_words.append("Verb 2: cannot be blank")
                    else:
                        for verb in verb_rows:
                            if v.lower() == verb.lower():
                                if k == "verb1":
                                    verb1_test = True
                                if k == "verb2":
                                    verb2_test = True
                        if verb1_test is not True:
                            if k == "verb1":
                                error_words.append("Verb 1: " + str(v))
                        if verb2_test is not True:
                            if k == "verb2":
                                error_words.append("Verb 2: " + str(v))
                case "adjective1" | "adjective2" | "adjective3":
                    if v == " " or v == "":
                        if k == "adjective1":
                            adjective1_test = False
                            error_words.append("Adjective 1: cannot be blank")
                        elif k == "adjective2":
                            adjective2_test = False
                            error_words.append("Adjective 2: cannot be blank")
                        elif k == "adjective3":
                            adjective3_test = False
                            error_words.append("Adjective 3: cannot be blank")
                    else:
                        for adjective in adjective_rows:
                            if v.lower() == adjective.lower():
                                if k == "adjective1":
                                    adjective1_test = True
                                if k == "adjective2":
                                    adjective2_test = True
                                if k == "adjective3":
                                    adjective3_test = True
                        if adjective1_test is not True and k == "adjective1":
                            error_words.append("Adjective 1: " + str(v))
                        if adjective2_test is not True and k == "adjective2":
                            error_words.append("Adjective 2: " + str(v))
                        if adjective3_test is not True and k == "adjective3":
                            error_words.append("Adjective 3: " + str(v))

                case "p_noun":
                    if v == " " or v == "":
                        p_noun_test = False
                        error_words.append("Plural noun: cannot be blank")
                    else:
                        for noun in plural_noun_rows:
                            if v.lower() == noun.lower():
                                p_noun_test = True
                        if p_noun_test is not True:
                            error_words.append("Plural Noun: " + str(v))
                case "noun1" | "noun2":
                    if v == " " or v == "":
                        if k == "noun1":
                            noun1_test = False
                            error_words.append("Noun 1: cannot be blank")
                        elif k == "noun2":
                            noun2_test = False
                            error_words.append("Noun 2: cannot be blank")
                    else:
                        for noun in noun_rows:
                            if v.lower() == noun.lower():
                                if k == "noun1":
                                    noun1_test = True
                                if k == "noun2":
                                    noun2_test = True
                        if noun1_test is not True and k == "noun1":
                            error_words.append("Noun 1: " + str(v))
                        if noun2_test is not True and k == "noun2":
                            error_words.append("Noun 2: " + str(v))
                case "name":
                    if v == " " or v == "":
                        name_test = False
                        error_words.append("Name cannot be blank")
                    else:
                        name_test = True
                case _:
                    raise ValueError
        # print(verb1_test)
        # print(verb2_test)
        # print(verb_ing_test)
        # print(adjective1_test)
        # print(adjective2_test)
        # print(adjective3_test)
        # print(p_noun_test)
        # print(noun1_test)
        # print(noun2_test)
        # print(name_test)
        if (verb1_test is False or verb2_test is False or verb_ing_test is False or p_noun_test is False or noun1_test
                is False or noun2_test is False or adjective1_test is False
                or adjective2_test is False or adjective3_test is False):
            words_pass_tf = False

            messagebox.showerror("Error!", "One or more of your words entered are not valid, please try again.      "
                                           "Check spelling, and make sure your word is a valid word     "
                                           "Errors in the following fields: " + str(error_words))
            error_words.clear()
            print(error_words)
        else:
            words_pass_tf = True
        return words_pass_tf
    except ValueError:
        print("Error, something went wrong")
    except Exception:
        print("Something went wrong")


def create_madlib():
    """
    Create a new madlib
    :return:
    """
    print("Creating Madlib")
    filled_words_dict = add_words_to_dict()
    print("Successfully added words to dict")
    passed_words = test_words(filled_words_dict)
    print("Successfully tested words")
    if passed_words is True:
        # Create new madlib
        madlib = ml.MadLib(passed_words)
        # active save madlib button
        save_madlib_button["state"] = "normal"
        start_button["state"] = "normal"
        # deactivate all entry fields
        create_madlib_button["state"] = "disabled"
        disable_text_fields()
        # reactivate start button
        start_button["state"] = "normal"
        # put the made madlib into the text field
        madlib_text["state"] = "normal"
        complete_madlib = madlib.gen_and_print_madlib()
        madlib_text.insert(1.0, (str(complete_madlib)))
        madlib_text["state"] = "disabled"
    else:
        # if words are not passed, start madlib and show error
        start_madlib()


def save_madlib():
    """
    Save madlib to external file
    :return:
    """
    # get text field, export out to a file
    try:
        f = open("myMadlib.txt", "a")
        f.write(madlib_text.get(1.0, "end-1c") + "\n \n")
        f.close()
    except IOError:
        print("File error")


def clear_text_fields():
    """
    Function to clear all text fields
    :return:
    """
    madlib_text["state"] = "normal"
    madlib_text.delete(1.0, "end-1c")
    madlib_text["state"] = "disabled"
    verb_text_1.delete(1.0, "end-1c")
    verb_text_2.delete(1.0, "end-1c")
    verb_text_3.delete(1.0, "end-1c")
    adjective_text_1.delete(1.0, "end-1c")
    adjective_text_2.delete(1.0, "end-1c")
    adjective_text_3.delete(1.0, "end-1c")
    noun_text_1.delete(1.0, "end-1c")
    noun_text_2.delete(1.0, "end-1c")
    plural_noun_text_1.delete(1.0, "end-1c")
    name_text.delete(1.0, "end-1c")


def disable_text_fields():
    """
    Function to disable all text fields
    :return:
    """
    verb_text_1["state"] = "disabled"
    verb_text_2["state"] = "disabled"
    verb_text_3["state"] = "disabled"
    adjective_text_1["state"] = "disabled"
    adjective_text_2["state"] = "disabled"
    adjective_text_3["state"] = "disabled"
    noun_text_1["state"] = "disabled"
    noun_text_2["state"] = "disabled"
    plural_noun_text_1["state"] = "disabled"
    name_text["state"] = "disabled"


def enable_text_fields():
    """
    Function to enable all text fields
    :return:
    """
    verb_text_1["state"] = "normal"
    verb_text_2["state"] = "normal"
    verb_text_3["state"] = "normal"
    adjective_text_1["state"] = "normal"
    adjective_text_2["state"] = "normal"
    adjective_text_3["state"] = "normal"
    noun_text_1["state"] = "normal"
    noun_text_2["state"] = "normal"
    plural_noun_text_1["state"] = "normal"
    name_text["state"] = "normal"


'''
Define functions/methods above here
'''

# create window
m = tkinter.Tk()
m.title('MadLib Game')
m.geometry("500x800")
m.config(bg='#ccffff')

'''
Insert Module Code Below Here
'''

welcome_label = tk.Label(text="Welcome To MadLibs!", bg='#ccffff')
welcome_label.grid(row=0, column=2)

start_game_label = tk.Label(text="Press the button to start the game:", bg='#ccffff')
start_game_label.grid(row=1, column=2)

start_button = (tk.Button(m, text="Start Game", width=10, command=start_madlib))
start_button.grid(row=2, column=2)

description = tk.Label(text="Enter different words below, that will be filled into the madlib!", bg='#ccffff')
description.grid(row=3, column=2)

verb_label_1 = tk.Label(text="Verb 1: ", bg='#ccffff')
verb_label_1.grid(row=4, column=1)
verb_text_1 = tk.Text(m, height=1, width=40, state="disabled")
verb_text_1.grid(row=4, column=2)

verb_label_2 = tk.Label(text="Verb 2: ", bg='#ccffff')
verb_label_2.grid(row=5, column=1)
verb_text_2 = tk.Text(m, height=1, width=40, state="disabled")
verb_text_2.grid(row=5, column=2)

verb_label_3 = tk.Label(text="Verb Ending in -ing: ", bg='#ccffff')
verb_label_3.grid(row=6, column=1)
verb_text_3 = tk.Text(m, height=1, width=40, state="disabled")
verb_text_3.grid(row=6, column=2)

adjective_label_1 = tk.Label(text="Adjective 1: ", bg='#ccffff')
adjective_label_1.grid(row=7, column=1)
adjective_text_1 = tk.Text(m, height=1, width=40, state="disabled")
adjective_text_1.grid(row=7, column=2)

adjective_label_2 = tk.Label(text="Adjective 2: ", bg='#ccffff')
adjective_label_2.grid(row=8, column=1)
adjective_text_2 = tk.Text(m, height=1, width=40, state="disabled")
adjective_text_2.grid(row=8, column=2)

adjective_label_3 = tk.Label(text="Adjective 3: ", bg='#ccffff')
adjective_label_3.grid(row=9, column=1)
adjective_text_3 = tk.Text(m, height=1, width=40, state="disabled")
adjective_text_3.grid(row=9, column=2)

noun_label_1 = tk.Label(text="Noun 1: ", bg='#ccffff')
noun_label_1.grid(row=10, column=1)
noun_text_1 = tk.Text(m, height=1, width=40, state="disabled")
noun_text_1.grid(row=10, column=2)

noun_label_2 = tk.Label(text="Noun 2: ", bg='#ccffff')
noun_label_2.grid(row=11, column=1)
noun_text_2 = tk.Text(m, height=1, width=40, state="disabled")
noun_text_2.grid(row=11, column=2)

plural_noun_label_1 = tk.Label(text="Plural Noun: ", bg='#ccffff')
plural_noun_label_1.grid(row=12, column=1)
plural_noun_text_1 = tk.Text(m, height=1, width=40, state="disabled")
plural_noun_text_1.grid(row=12, column=2)

name_label = tk.Label(text="Name: ", bg="#ccffff")
name_label.grid(row=13, column=1)
name_text = tk.Text(m, height=1, width=40, state="disabled")
name_text.grid(row=13, column=2)

create_madlib_button = tk.Button(m, text="Create MadLib", width=12, command=create_madlib, state="disabled")
create_madlib_button.grid(row=14, column=2)

madLib_label = tk.Label(text="Your MadLib:", bg='#ccffff')
madLib_label.grid(row=15, column=2)

madlib_text = tk.Text(m, height=20, width=40, state="disabled")
madlib_text.grid(row=16, column=2)

save_madlib_label = tk.Label(text="Save your MadLib to a file!", bg='#ccffff')
save_madlib_label.grid(row=17, column=2)
save_madlib_button = tk.Button(m, text="Save Madlib", width=12, command=save_madlib, state="disabled")
save_madlib_button.grid(row=18, column=2)

start_over_label = tk.Label(text="Start a new MadLib by Pressing Start Game!", bg='#ccffff')
start_over_label.grid(row=19, column=2)

'''
Insert module code above here
'''
m.mainloop()
