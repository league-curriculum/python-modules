"""
Python logic operators: and, or
"""
from tkinter import messagebox, simpledialog, Tk

# The Python keywords 'and' and 'or' are used to test if multiple boolean
# conditions are true or false. For example:
#   if name == 'Sally' or name == 'Sue':
#       print('Your name is either Sally or Sue!')
# The 'or' checks if either the first condition (name == 'Sally') is true or
# the second condition (name == 'Sue') is true. If either condition is true,
# the entire expression is true.
#
# The 'and' checks that both conditions are true for the entire expression to
# be true. For example:
#   if age > 12 and height_inches > 48:
#       print('You can ride the roller coaster!')
# The print function will only be called if age is greater than 12 and
# height_inches is greater than 48. If any conditions is false, the print
# function will not be called
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    name = simpledialog.askstring(None, "What is your name?")

    if name == 'Sally' or name == 'Sue':
        messagebox.showinfo(None, 'Your name is either Sally or Sue!')
    else:
        messagebox.showwarning(None, 'Your name is NOT Sally or Sue')

    age = simpledialog.askinteger(None, "How old are you?")
    height_inches = simpledialog.askinteger(None, "What is your height in inches?")

    if age > 12 and height_inches > 48:
        messagebox.showinfo(None, 'You can ride the roller coaster!')
    else:
        messagebox.showerror(None, 'You are not tall enough and old enough to ride the roller coaster')
