import random
from tkinter import messagebox, Tk


window = Tk()
window.withdraw()

for i in range(10):
    randomNumber = random.randint(1, 5)

    print(randomNumber)

    # TODO 1) Use each value of randomNumber to give the user a random compliment.  Use the messagebox.showinfo() function to display the compliment
    if randomNumber == 1:  # ;
        messagebox.showinfo(None, "You are awesome")  # ;
    elif randomNumber == 2:  # ;
        messagebox.showinfo(None, "You are smart")  # ;
    elif randomNumber == 3:  # ;
        messagebox.showinfo(None, "I like your shirt")  # ;
    elif randomNumber == 4:  # ;
        messagebox.showinfo(None, "You are funny")  # ;
    else:  # ;
        messagebox.showinfo(None, "I like your shoes")  # ;

        # TODO 2) Repeat all the code above 10 times

        # TODO 3) Find someone to test out your program. They will like it :)
