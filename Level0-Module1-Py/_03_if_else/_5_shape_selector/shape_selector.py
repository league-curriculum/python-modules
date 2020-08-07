import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    my_turtle = turtle.Turtle()
    my_turtle.shape('turtle')
    my_turtle.pendown()

    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(None, 'What kind of shape do you want to draw?')

    # Draw the shape requested by the user using if-elif-else statements
    if shape == 'triangle':
        my_turtle.circle(100, 360, steps=3)
    elif shape == 'square':
        my_turtle.right(45)
        my_turtle.circle(100, 360, steps=4)
    elif shape == 'circle':
        my_turtle.circle(100, 360, steps=50)
    else:
        messagebox.showerror(None, "I don't know how to draw a " + shape)

    # Call the turtle .done() method
    turtle.done()
    window.mainloop()