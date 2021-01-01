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

    # TODO: String can also be converted to integers using the int() function
    #  The first pop-up combines the 2 strings "3" and '7' to get "37"
    #  When converted to integers, the + does an arithmetic add to get 10
    num1_str = '3'
    num2_str = '7'
    messagebox.showinfo(None, num1_str + num2_str)
    messagebox.showinfo(None, int(num1_str) + int(num2_str))

    # TODO: Uncomment the code below and run the program again
    #   Use str() to print num1 and num2
    # messagebox.showinfo(None, "num1 = " + num1 + " num2 = " + num2)
