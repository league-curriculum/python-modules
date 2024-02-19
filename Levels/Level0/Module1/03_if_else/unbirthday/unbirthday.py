from tkinter import messagebox, simpledialog, Tk


"""
Ask the user for their birthday (mm/dd), e.g. 06/09

'If' it matches today's date, wish them a happy birthday

Otherwise 'else', wish them a very merry UNbirthday
"""

# Hint: use simpledialog.askstring() to get the user's birthday

birthday = simpledialog.askstring(None, "When is your birthday (mm/dd)?")  # ;

if birthday == "08/07":  # ;
    messagebox.showinfo(None, "Happy Birthday!")  # ;
else:  # ;
    messagebox.showinfo(None, "Happy UN-Birthday!")  # ;
