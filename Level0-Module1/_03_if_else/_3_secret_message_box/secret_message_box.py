from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    pw = simpledialog.askstring(None, 'Enter a password')

    secret_message = simpledialog.askstring(None, 'Enter a secret message')

    guess_pw = simpledialog.askstring(None, 'Enter the password if you want to see the secret message')

    if guess_pw == pw:
        messagebox.showinfo(None, 'Here is the secret message: ' + secret_message)
    else:
        messagebox.showerror(None, 'INCORRECT: Intruder Alter!!!!')

    window.mainloop()