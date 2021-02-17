# Write a Python program that asks the user for two numbers.
# Then ask the user if the would like to add, subtract, multiply, or divide.
# Use if-else statements to provide the desired math operation on the numbers and display the result.
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    num1 = simpledialog.askfloat(None, 'Enter a number')
    num2 = simpledialog.askfloat(None, 'Enter a second number')
    operation = simpledialog.askstring(None, 'Enter a math operation (multiple, divide, add, subtract)')
    result = None

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        messagebox.showerror(None, 'ERROR: unknown operation ' + operation)

    messagebox.showinfo(None, "The " + operation + " of " + str(num1) + " and " + str(num2) + " = " + str(result))

    window.mainloop()