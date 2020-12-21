from tkinter import Tk, Label, Button

from PIL import ImageTk, Image


def onclick(args):
    if args == 1:
        print("rock")
    if args == 2:
        print("paper")
    if args == 3:
        print("scissors")


if __name__ == '__main__':
    window = Tk()
    window.title("Join")
    window.geometry("1075x250")
    window.configure(background="grey")

    Label(window, text="Choose Your Weapon!", bg="grey").pack(side="left")

    img_rock = ImageTk.PhotoImage(file="rock.png")
    img_paper = ImageTk.PhotoImage(file="paper.jpeg")
    img_scissors = ImageTk.PhotoImage(file="scissors.jpeg")

    Button(window, image=img_rock, command=lambda: onclick(1)).pack(side="left")
    Button(window, image=img_paper, command=lambda: onclick(2)).pack(side="left")
    Button(window, image=img_scissors, command=lambda: onclick(3)).pack(side="left")

    # Start the GUI
    window.mainloop()
