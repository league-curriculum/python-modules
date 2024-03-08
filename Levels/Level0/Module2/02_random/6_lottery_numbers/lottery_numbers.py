import random
from tkinter import messagebox, Tk, simpledialog


window = Tk()
window.withdraw()

lotteryNum = ""
# TODO 1) Get 6 random numbers from 1 to 100 to put on your lottery ticket
for i in range(6):  # ;
    randNum = random.randint(1, 100)  # ;
    lotteryNum += str(randNum) + ", "  # ;

# TODO 2) Display the selected numbers to the user in a pop-up

messagebox.showinfo("Winning Lottery Ticket", lotteryNum)  # ;
# TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
