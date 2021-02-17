from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    birthday = simpledialog.askstring(None, "When is your birthday (mm/dd)?")

    if birthday == "08/07":
        messagebox.showinfo(None, "Happy Birthday!")
    else:
        messagebox.showinfo(None, "Happy UN-Birthday!")
