"""
Log Search using a Id-Name Dictionary
"""

# TODO: Create a dictionary of integers for the keys and strings for the values.
#  Create a GUI app with three buttons. Look at 'log_search_example.png' in this
#  folder for an example of what your program should look like.
#
#  Button 1: Add Entry
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      After an ID is entered, use another input dialog to ask the user
#      to enter a name. Add this information as a new entry to your
#      dictionary.

#  Button 2: Search by ID
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      If that ID exists, display that name to the user.
#      Otherwise, tell the user that that entry does not exist.
#
# Button 3: View List
#      When this button is clicked, display the entire list in a message
#      dialog in the following format:
#      ID: 123  Name: Harry Howard
#      ID: 245  Name: Polly Powers
#      ID: 433  Name: Oliver Ortega
#      etc...
#
# When this is complete, add a fourth button to your window.
# Button 4: Remove Entry
#      When this button is clicked, prompt the user to enter an ID using
#      an input dialog.
#      If this ID exists in the dictionary, remove it. Otherwise, notify the
#      user that the ID is not in the list.
#
import tkinter as tk
from tkinter import simpledialog, messagebox

