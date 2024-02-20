from tkinter import messagebox, simpledialog, Tk


window = Tk()  # ;
window.withdraw()  # ;

name = simpledialog.askstring(None, "What is your name?")  # ;

if name.lower() == "daniel":  # ;
    messagebox.showinfo(None, "Hi " + name + " you are great at coding Python!")  # ;
elif name.lower() == "dave":  # ;
    messagebox.showinfo(None, "Hi " + name + " you are great at teaching")  # ;
else:  # ;
    messagebox.showinfo(None, "Hi " + name + ", nice to meet you!")  # ;

window.mainloop()  # ;
