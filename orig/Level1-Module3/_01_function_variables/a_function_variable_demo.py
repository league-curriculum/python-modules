"""
Storing functions as variables
"""

# Functions and methods can be stored in a variable like so,
#   def func():
#       print('Calling func()!!!')
#
#   var = func
#
# The variable 'var' holds a reference to the function 'func'.
# This means that 'func' can be called using the 'var' variable.
# For example:
#   var()       # prints 'Calling func()!!!'
#
# This works if the function has input variables as well:
#   def add(var_1, var_2):
#       return var_2 + var_2
#
#   var = add
#   var(1, 2)   # returns 3
#
# This feature can be useful if the code needs to call the function at
# a later time. Run the code below for another example:
import tkinter as tk

class FunctionVariableExample(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self, text='func variable', bg='white', font=('Arial', 20, 'normal'))
        self.button.pack()

        # Notice the difference between binding the button press to the
        # same method with () and without.
        #
        # Writing self.on_button_press(None) means the method gets called
        # immediately BEFORE pressing the button when the object is created.
        # If the method name is used without the (), the method doesn't get
        # called until the button is pressed.
        self.button.bind('<ButtonPress>', self.on_button_press(None))
        #self.button.bind('<ButtonPress>', self.on_button_press)

    def on_button_press(self, event):
        self.button.configure(bg='blue', text='on_button_press_1')
        self.button.pack()

if __name__ == '__main__':
    app = FunctionVariableExample()
    app.mainloop()
