# Write a Python program that asks the user for two numbers. 
# Then display the sum of the two numbers
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    num1 = simpledialog.askfloat(None, 'Enter a number')
    num2 = simpledialog.askfloat(None, 'Enter a second number')

    messagebox.showinfo(None, "The sum of " + str(num1) + " and " + str(num2) + " = " + str(num1+num2))

    window.mainloop()