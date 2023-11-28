"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 11/28/23

MadLib Final Project, gui
"""
import tkinter
import tkinter as tk

'''
Define functions/methods below here
'''

madLib_number = 0

def start_madlib():
    # activate all fields
    # activate create madlib button
    pass


def create_madlib():
    # test all inputs before moving on
    # Create new madlib
    # parameters: words_dict and madlib_number
    # active save madlib button
    # activate start new madlib button
    # deactivate all entry fields
    pass


def save_madlib():
    #File out
    pass


def start_new_madlib():
    # activate and clear all fields
    # deactive start over and save madlib buttons
    # clear results text field
    pass

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
adjective_label_1 = tk.Text(m, height=1, width=40, state="disabled")
adjective_label_1.grid(row=7, column=2)

adjective_label_2 = tk.Label(text="Adjective 2: ", bg='#ccffff')
adjective_label_2.grid(row=8, column=1)
adjective_label_2 = tk.Text(m, height=1, width=40, state="disabled")
adjective_label_2.grid(row=8, column=2)

adjective_label_3 = tk.Label(text="Adjective 3: ", bg='#ccffff')
adjective_label_3.grid(row=9, column=1)
adjective_label_3 = tk.Text(m, height=1, width=40, state="disabled")
adjective_label_3.grid(row=9, column=2)

noun_label_1 = tk.Label(text="Noun 1: ", bg='#ccffff')
noun_label_1.grid(row=10, column=1)
noun_label_1 = tk.Text(m, height=1, width=40, state="disabled")
noun_label_1.grid(row=10, column=2)

noun_label_2 = tk.Label(text="Noun 2: ", bg='#ccffff')
noun_label_2.grid(row=11, column=1)
noun_label_2 = tk.Text(m, height=1, width=40, state="disabled")
noun_label_2.grid(row=11, column=2)

plural_noun_label_1 = tk.Label(text="Plural Noun: ", bg='#ccffff')
plural_noun_label_1.grid(row=12, column=1)
plural_noun_label_1 = tk.Text(m, height=1, width=40, state="disabled")
plural_noun_label_1.grid(row=12, column=2)

create_madlib_button = tk.Button(m, text="Create MadLib", width=12, command=create_madlib)
create_madlib_button.grid(row=13, column=2)

madLib_label = tk.Label(text="Your MadLib:", bg='#ccffff')
madLib_label.grid(row=14, column=2)

madlib_text = tk.Text(m, height=20, width=40, state="disabled")
madlib_text.grid(row=15, column=2)

save_madlib_label = tk.Label(text="Save your MadLib to a file!", bg='#ccffff')
save_madlib_label.grid(row=16, column=2)
save_madlib_bttn = tk.Button(m, text="Save Madlib", width=12, command=save_madlib, state="disabled")
save_madlib_bttn.grid(row=17, column=2)

start_over_label = tk.Label(text="Start a new MadLib!", bg='#ccffff')
start_over_label.grid(row=18, column=2)
start_over_bttn = tk.Button(m, text="Start Over", width=12, command=start_new_madlib, state="disabled")
start_over_bttn.grid(row=19, column=2)
'''
Insert module code above here
'''
m.mainloop()
