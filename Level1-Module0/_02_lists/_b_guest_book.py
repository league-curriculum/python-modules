from tkinter import messagebox, simpledialog, Tk
import tkinter as tk


class GuestBook(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)

        self.guests = list()

        self.geometry('250x50')

        self.grid()

        button_add = tk.Button(self, text='Add Guest', command=lambda : self.add_guest())
        button_add.grid(padx=20, pady=10, row=0, column=0)

        button_print_guests = tk.Button(self, text='View Guests', command=lambda : self.print_guests())
        button_print_guests.grid(padx=20, pady=10, row=0, column=1)

    def add_guest(self):
        guest = simpledialog.askstring(None, prompt="Enter the new Guest's name")

        if guest is not None:
            self.guests.append(guest)

    def print_guests(self):
        guest_list = str()

        for i, guest in enumerate(self.guests):
            guest_list += 'Guest #' + str(i+1) + '. ' + guest

            if i != (len(self.guests) - 1):
                guest_list += '\n'

#        guest_list = ''.join([ 'Guest #' +str(i+1) + '. ' + guest + '\n' for i, guest in enumerate(self.guests)])

        messagebox.showinfo('Guests', guest_list)


if __name__ == '__main__':
    gb = GuestBook(None)
    gb.title('Guest Book')
    gb.mainloop()