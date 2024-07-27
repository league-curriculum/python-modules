
# Getting Started with Python

This is the first formal lesson of your first Python class with the Leage of
Amazing Programmers. To follow these lessons, you should be reading this file in
Visual Studio Code if you are on your own computer, or if you are using a
website, it should be Github Codespaces. For the first step, be that this text
looks nice, not like a text file. If the title at the top of the page looks like
 "# Getting Started with Python" the right-click on the name of the file and
select "Open Preview", or hit "⇧ Alt V" or "⇧ ⌘ V". Now you should be able to
see our flag logo here: <img style="vertical-align:middle" src="https://images.jointheleague.org/logos/flag.png" height="25px" >

## Open a Virtual Screen on the Web

If you started your editor as a Codespace on Github, that is, you clicked
on a button like <img style="vertical-align:middle" src="https://images.jointheleague.org/vscode/create_codespace.png" height="25px" > 
to start your editor, then you need to follow these steps to open a virtual screen. 
Your Codespace is running your code in a data center far away, and it doesn't have a screen,
so if you want to see your program output, you have to create a virtual screen. 

In the bottom pane of the VSCode window, click on the "PORTS" tab. ( If you don't see a 
"PORTS" tab, you probably can skip this step. )

<center><img src="https://images.jointheleague.org/module-navigation/ports_pane.png" width="600px"></center>

Hover over the "Forwarded Address" for port 6080. You will see a small icon
that looks like a split box with a magnifying lens Click on it. This will
open a new browser window with a "noVNC" logo. 

You might need to drag the browser window to the right side of the screen. Your
screen should look something like:

<center><img src="https://images.jointheleague.org/module-navigation/browser_window.png" width="600px"></center>

Click on "Connect". If it asks for a password,  enter the passwod: "code4life"


Now you have a virtual screen running. When your program writes to the screen, it will show up in this window. 

# Running Programs

Here is a simple program, one that you might have seen before. It is a simple
Turtle program that draws a square and writes a message. The lines that start
with a # are comments. They are not executed by Python. Comments are used to
explain what the code does. Read the program and try to understand what each
line does.

```python

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 
forward = 150                           # Set the forward distance to 150
left = 90                               # Set the left turn to 90 degrees

tina.pencolor('blue')                   # Set the pen color to blue
tina.forward(forward)                   # Move tina forward by the forward distance
tina.left(left)                         # Turn tina left by the left turn

tina.pencolor('red')                    # Set the pen color to red
tina.forward(forward)                   # Continuie the last two steps three more times
tina.left(left)                         # to draw a square

tina.pencolor('green')                  # Set the pen color to green
tina.forward(forward)
tina.left(left)

tina.pencolor('purple')                 # Set the pen color to purple
tina.forward(forward)
tina.left(left)

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.forward(20)                        # Move tina forward by 20
tina.left(left)                         # Turn tina left by 90 degrees
tina.forward(20)                        # Move tina forward by 20
tina.write("Why, hello there!")         # Write the message "Why, hello there!"
tina.backward(20)                       # Move tina backward by 20

turtle.exitonclick()                    # Close the window when we click on it
```
 
This program has been copied into the next file in this module, which is named
``02_Meet_Tina.py``.  To run the program:

1. Click on the file name to open the file
2. Look in the upper right for these icons: <img style="vertical-align:middle" src="https://images.jointheleague.org/vscode/run_buttons.png" height="25px" > 
    click on the ▶️ run button to run the program.  
3. Click on the window to close it. 