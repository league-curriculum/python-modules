"""
* Create an app like the one shown in the pictures in this package,
  'guest_book_add.png' and 'guest_book_print'
"""
from tkinter import messagebox, simpledialog, Tk
import tkinter as tk

# TODO 1) Complete the function by:
#         a. Asking for the name of the guest to add
#         b. Add the guest to list_of_guests
#         c. Return the list_of_guests
def add_guest(list_of_guests):
    guest = None

    while guest is None:
        guest = simpledialog.askstring(None, prompt="Enter the new Guest name to add")

    list_of_guests.append(guest)

    return list_of_guests

# TODO 2) Complete the function by:
#         a. Asking for the name of the guest to remove
#         b. Remove the guest from list_of_guests. Do not change the list if
#            the guest isn't in the list.
#         c. Return the list_of_guests
def remove_guest(list_of_guests):
    guest = None

    while guest is None:
        guest = simpledialog.askstring(None, prompt="Enter the Guest name to remove")

    try:
        list_of_guests.remove(guest)
    except ValueError:
        messagebox.showerror("ERROR", str(guest) + ' is not a guest on the guest list')

    return list_of_guests

# TODO 3) Complete the function by:
#         a. Display the names of the guests in the following format:
#            Guest 1. Alan
#            Guest 2. Maria
#            Guest 3. Jin
#         b. If there are no guests, print "There are no guests"
def print_guests(list_of_guests):
    guest_list = str()

    for i, guest in enumerate(list_of_guests):
        guest_list += 'Guest #' + str(i + 1) + '. ' + guest

        if i != (len(list_of_guests) - 1):
            guest_list += '\n'

    # Alternate way
    # guest_list = ''.join([ 'Guest #' +str(i+1) + '. ' + guest + '\n' for i, guest in enumerate(self.guests)])

    messagebox.showinfo('Guests', guest_list)


# 4. Create an app like the one show in the pictures in this package, 'guest_book_add.png'
# and 'guest_book_print'
class GuestBook(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)

        self.guests = list()

        self.geometry('260x50')

        self.grid()

        button_add = tk.Button(self, text='Add Guest', command=self.add_guest)
        button_add.grid(padx=5, pady=10, row=0, column=0)

        button_remove = tk.Button(self, text='Remove Guest', command=self.remove_guest)
        button_remove.grid(padx=5, pady=10, row=0, column=1)

        button_print_guests = tk.Button(self, text='View Guests', command=self.print_guests)
        button_print_guests.grid(padx=5, pady=10, row=0, column=2)

    def add_guest(self):
        self.guests = add_guest(self.guests)

    def remove_guest(self):
        self.guests = remove_guest(self.guests)

    def print_guests(self):
        print_guests(self.guests)


if __name__ == '__main__':
    gb = GuestBook(None)
    gb.title('Guest Book')
    gb.mainloop()
