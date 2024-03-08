import random
from tkinter import Label, Button, Tk

from PIL import ImageTk
import os


window = Tk()
window.title("Roll the Dice!")

current_directory = os.path.dirname(__file__)

dice1 = ImageTk.PhotoImage(file=os.path.join(current_directory, "dice 1.png"))
dice2 = ImageTk.PhotoImage(file=os.path.join(current_directory, "dice 2.png"))
dice3 = ImageTk.PhotoImage(file=os.path.join(current_directory, "dice 3.png"))
dice4 = ImageTk.PhotoImage(file=os.path.join(current_directory, "dice 4.png"))
dice5 = ImageTk.PhotoImage(file=os.path.join(current_directory, "dice 5.png"))
dice6 = ImageTk.PhotoImage(file=os.path.join(current_directory, "dice 6.png"))

label = Label(window, image=dice1)
label.pack(side="left")


def onclick(args):
    if args == "button":
        # TODO 1) Make random_choice equal to a random number between 1 and 6
        random_choice = random.randint(1, 6)  # ;

        # TODO 2) Fix the code below so that the random image is displayed when the button is clicked.  Hint: None is not a valid number
        if random_choice == None:
            label.configure(image=dice1)
            label.image = dice1
        elif random_choice == None:
            label.configure(image=dice2)
            label.image = dice2
        elif random_choice == None:
            label.configure(image=dice3)
            label.image = dice3
        elif random_choice == None:
            label.configure(image=dice4)
            label.image = dice4
        elif random_choice == None:
            label.configure(image=dice5)
            label.image = dice5
        else:
            label.configure(image=dice6)
            label.image = dice6


Button(window, text="CLICK HERE TO ROLL", command=lambda: onclick("button")).pack(
    side="left"
)

# Start the GUI
window.mainloop()
