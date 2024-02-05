import turtle
from PIL import Image

# ================= Instructions at the bottom of this file ===================

def set_background(filename):
    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(filename)
    rootwindow = window.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
    
def initialize_turtle(my_turtle):
    my_turtle.hideturtle()
    my_turtle.shape('turtle')
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.goto(-95,-265)
    my_turtle.setheading(90)
    my_turtle.speed(3)
    my_turtle.color('#1DA1F2')
    my_turtle.pen(pendown=True, pencolor='#1DA1F2', pensize=4, outline=0)
    my_turtle.showturtle()
    return my_turtle


if __name__ == '__main__':
    window = turtle.Screen()
    set_background('simplemaze.png')
    
    # ====================== DO NOT EDIT THE CODE ABOVE ===========================
    
    # TODO) 1. Create a Turtle object and initialize it with initialize_turtle()
    my_turtle = turtle.Turtle()
    my_turtle = initialize_turtle(my_turtle)
    
    # TODO) 2. Use the open() function and "with" to start 
    #          reading "turtle_gps.txt" in python
    # with open("turtle_gps.txt", "r") as f:
    with open("turtle_gps.txt", "r") as f:
        
    # TODO) 3. Use a for loop inside the "with" to iterate 
    #          through the file lines
    #     for line in f:
        for line in f:
        
    # TODO) 4. Use if statements to interpret each line in the file 
    #          and get the turtle to navigate the maze.
    #          FORWARD should use my_turtle.forward()
    #          RIGHT should use my_turtle.right()
    #          LEFT should use my_turtle.left()
            command, value = line.strip().split()
            value = int(value)
            if command == 'FORWARD':
                my_turtle.forward(value)
            elif command == 'RIGHT':
                my_turtle.right(value)
            elif command == 'LEFT':
                my_turtle.left(value)
                
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    
    turtle.done()
    
    # Windows compatibility: https://stackoverflow.com/questions/50438762/python-turtle-window-crashes-every-2nd-time-running 
    from sys import platform
    if platform == 'win32':
        turtle.bye() 