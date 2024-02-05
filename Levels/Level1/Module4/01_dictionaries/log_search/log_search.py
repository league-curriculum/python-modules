"""
Log Search using a Id-Name Dictionary
"""

#
# Create a dictionary of integers for the keys and strings for the values.
# Create a GUI app with three buttons.
#
# Button 1: Add Entry
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      After an ID is entered, use another input dialog to ask the user
#      to enter a name. Add this information as a new entry to your
#      dictionary.
#
# Button 2: Search by ID
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


class Log(tk.Tk):
    def __init__(self):
        super().__init__()

        self.entries = dict()

        self.button_add = tk.Button(self, text='Add')
        self.button_search = tk.Button(self, text='Search')
        self.button_view = tk.Button(self, text='View')
        self.button_remove = tk.Button(self, text='Remove')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.button_add.grid(row=0, column=0)
        self.button_search.grid(row=0, column=1)
        self.button_view.grid(row=0, column=2)
        self.button_remove.grid(row=0, column=3)

        self.button_add.bind('<ButtonPress>', self.add)
        self.button_search.bind('<ButtonPress>', self.search)
        self.button_view.bind('<ButtonPress>', self.view)
        self.button_remove.bind('<ButtonPress>', self.remove)

    def add(self, event):
        id_key = simpledialog.askstring(title='Add: ID', prompt='Enter the ID')

        if not id_key.isdigit():
            messagebox.showerror('ERROR: Invalid ID', 'ERROR: ID not all digits')
            return

        name_value = simpledialog.askstring(title='Add: name', prompt='Enter the corresponding name')
        ok = messagebox.askquestion('Confirm', message='Add ' + id_key + ' : ' + name_value)
        if ok == 'yes':
            self.entries[id_key] = name_value
            messagebox.showinfo('Added', message='Added ' + id_key + ' : ' + name_value)

    def search(self, event):
        id_key = simpledialog.askstring(title='Search: ID', prompt='Enter the ID')
        if id_key in self.entries:
            name_value = self.entries[id_key]
            messagebox.showinfo('Search: ID', id_key + ' corresponds to ' + str(name_value))
        else:
            messagebox.showerror('ERROR: Not Found', 'ERROR: ' + id_key + ' was not found!')

    def view(self, event):
        log = str()

        for id_key, name_value in self.entries.items():
            log += str(id_key) + ' : ' + str(name_value) + '\n'

        messagebox.showinfo('View', log)

    def remove(self, event):
        id_key = simpledialog.askstring(title='Remove: ID', prompt='Enter the ID to remove')
        ok = messagebox.askquestion(None, 'Remove ID ' + id_key + '?')
        if ok == 'yes':
            if id_key in self.entries:
                del self.entries[id_key]
                messagebox.showinfo('Remove: ID', 'ID ' + id_key + ' was removed.')
            else:
                messagebox.showerror('ERROR: ID Not Found', 'ERROR: ID ' + id_key + ' was not found.')


app = Log()
app.title('Log Search')
app.geometry('250x50')
app.mainloop()
