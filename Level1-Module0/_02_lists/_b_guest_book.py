from tkinter import messagebox, simpledialog, Tk
import tkinter as tk


# 4. Create an app like the one show in the pictures in this package, 'guest_book_add.png'
# and 'guest_book_print'
class GuestBook(tk.Tk):

    def __init__(self, parent):
        super().__init__(parent)


if __name__ == '__main__':
    # 1. Make a new GuestBook
    gb = GuestBook(None)

    # 2. Set the title
    gb.title('Guest Book')

    # 3. Run your game's mainloop
    gb.mainloop()
