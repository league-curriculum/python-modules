from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO: Run the program to see the difference between the 2 pop-ups
    #   The 2nd pop-up does not add the 2 numbers
    #   str() changes a number to a word(string)
    #   We are adding "3" + "7" to get 37
    num1 = 3
    num2 = 7
    messagebox.showinfo(None, num1 + num2)
    messagebox.showinfo(None, str(num1) + str(num2))

    # TODO: Uncomment the code below and run the program again
    #   Using str() we can use words and numbers together
    messagebox.showinfo(None, "num1 = " + str(num1) + " num2 = " + str(num2))

