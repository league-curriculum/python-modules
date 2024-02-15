# Imports go at the top
from microbit import *
from random import randint
from time import sleep

# Matrix in column major format
column = [[0]*5]
m = column * 5

m = [
 (0, 0, 3, 0, 0),
 (0, 3, 6, 3, 0),
 (3, 6, 9, 6, 3),
 (0, 3, 6, 3, 0),
 (0, 0, 3, 0, 0)
]

def add_col(m, c):
    """ Add a column to the front, remove one from the rear"""
    return [c]+m[0:4]

def make_image(m):

    def row(r):
        return ''.join(str(e) for e in r) + ":"

    t = list(zip(*m))
    return Image(''.join(row(r) for r in t)  )

def int_to_row(v):
    v = min(v, 44)
    n = v // 9
    r = v - (n*9)
    row = [9]*n + [r]
    
    return (row + ([0] * (5-len(row))))[::-1]


while True:

    v = pin0.read_analog()
    s = scale(v, from_=(0,1024), to=(0,44))
    m = add_col(m, int_to_row(s))
    print(v,s )
    i = make_image(m)
    display.show(i)
    sleep(.1)
    
