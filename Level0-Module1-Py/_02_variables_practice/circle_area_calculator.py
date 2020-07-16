import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    window = Tk()
    
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    radius = simpledialog.askinteger(title='', prompt='radius in pixels?')
    
    # Make a new turtle
    daniel = turtle.Turtle()
    
    # Have your turtle draw a circle with the correct radius
    daniel.circle(radius=radius, extent=360, steps=30)

    # Call the turtle .penup() method
    daniel.penup()

    # Move your turtle to a new x,y position using .goto()
    daniel.goto(-50, -50)

    # Calculate the area of your circle and store it in a variable, you can use math.pi
    area = radius*radius*math.pi
    
    # Write the area of your circle using the turtle .write() method
    # myTurtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    daniel.write(arg="area = " + str(area), move=False, align='left', font=('Arial',8,'normal'))

    # Hide your turtle
    daniel.hideturtle()

    window.mainloop()
    turtle.done()