# This is a program to show how functions can be used just like variables

import tkinter
import math

# The drawGraph function takes a function as a parameter
# and draws that function as a graph
def drawGraph(func):
    root = tkinter.Tk()
    width = 700
    height = 700
    cvs = tkinter.Canvas(root, bg="white", height=width, width=height)
    cvs.create_line(0, height / 2, width, height / 2)
    cvs.create_line(width / 2, 0, width / 2, height)
    lastY = func(0)
    for i in range(1, width):
        y = func(i - (width / 2))
        cvs.create_line(i - 1, height - (lastY + (height / 2)), i, height - (y + (height / 2)), width=2, fill="blue")
        lastY = y


    cvs.pack()
    root.mainloop()

# Here are some example functions. The functions must take in
# an X value and return a y value.
def parabola(x):
    hx = x * 0.1
    return (hx * hx) - 300

def sinWave(x):
    return math.sin(x * 0.03) * 100

def cubic(x):
    hx = x * 0.03
    return (hx * hx * hx)

# 1. Create THREE (3) more functions.

if __name__ == "__main__":
    drawGraph(parabola)
    drawGraph(sinWave)
    drawGraph(cubic)

    #2. draw the graph of your functions to see if they look correct.