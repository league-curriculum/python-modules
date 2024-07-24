"""
Create a simple calculator app
"""
import tkinter as tk

class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()

        self.entry1 = tk.Entry(self)
        self.entry1.place(relx=0.05, rely=0.1, relwidth=0.4)

        self.entry2 = tk.Entry(self)
        self.entry2.place(relx=0.5, rely=0.1, relwidth=0.4)

        button_add = tk.Button(self, text='add', command=lambda : self.add())
        button_add.place(relx=0.025, rely=0.3, relwidth=0.2, relheight=0.1)

        button_subtract = tk.Button(self, text='subtract', command=lambda : self.subtract())
        button_subtract.place(relx=0.25, rely=0.3, relwidth=0.2, relheight=0.1)

        button_multiply = tk.Button(self, text='multiply', command=lambda : self.multiply())
        button_multiply.place(relx=0.475, rely=0.3, relwidth=0.2, relheight=0.1)

        button_divide = tk.Button(self, text='divide', command=lambda : self.divide())
        button_divide.place(relx=0.7, rely=0.3, relwidth=0.2, relheight=0.1)

        # Alternative way to do this using StringVar
        #self.result = tk.StringVar()
        #self.label_result = tk.Label(self, text='hello', font=('arial', 32, 'bold'), textvariable=self.result)
        self.label_result = tk.Label(self, text='hello', font=('arial', 32, 'bold'))
        self.label_result.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)

    def add(self):
        num1 = float(self.entry1.get())
        num2 = float(self.entry2.get())
        self.label_result.configure(text=str(num1 + num2))

        # If using StringVar
        #self.result.set(num1 + num2)

    def subtract(self):
        num1 = float(self.entry1.get())
        num2 = float(self.entry2.get())
        self.label_result.configure(text=str(num1 - num2))

        # If using StringVar
        #self.result.set(num1 - num2)

    def multiply(self):
        num1 = float(self.entry1.get())
        num2 = float(self.entry2.get())
        self.label_result.configure(text=str(num1 * num2))

        # If using StringVar
        #self.result.set(num1 * num2)

    def divide(self):
        num1 = float(self.entry1.get())
        num2 = float(self.entry2.get())
        self.label_result.configure(text=str(num1 / num2))

        # If using StringVar
        #self.result.set(num1 / num2)



c = Calculator()
c.title('Calculator')
c.geometry('400x200')
c.mainloop()
