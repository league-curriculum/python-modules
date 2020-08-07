'''
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got correct
'''
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    answer = simpledialog.askstring(None, 'Why did the bike fall to the ground?')

    if 'two' in answer and 'tired' in answer:
        messagebox.showinfo(None, 'Correct!!!!')
    else:
        messagebox.showinfo(None, 'Incorrect! It fell over because it was TWO TIRED!')

    window.mainloop()