"""
* Create an app like the one shown in the pictures in this package,
  'guest_book_add.png' and 'guest_book_print'
"""
from tkinter import messagebox, simpledialog, Tk
import tkinter as tk


class GuestBook(tk.Tk):
    def __init__(self, parent):
        super().__init__(parent)


if __name__ == '__main__':
    gb = GuestBook(None)

    gb.title('Guest Book')

    gb.mainloop()
