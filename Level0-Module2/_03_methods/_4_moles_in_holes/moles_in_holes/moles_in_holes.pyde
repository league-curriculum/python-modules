# When you are done, this program will draw a mole in 
# each of the holes.

def setup():
     size(400, 400)
     background(78, 166, 51) # green grass
     
     # This code draws the holes. Run the program to see them.
     
     fill(0, 0, 0)
     ellipse(200, 200, 100, 30)
     ellipse(70, 119, 100, 30)
     ellipse(300, 60, 100, 30)
     ellipse(297, 350, 100, 30)

def draw():

    # Write code here that uses the drawMole method to put a mole in each of the holes
   



def drawMole(moleX, moleY):
     noStroke()
     fill(125, 93, 43)
     ellipse(moleX, moleY, 60, 60) # face
     fill(255, 237, 209)
     ellipse(moleX, moleY+10, 33, 28) 
     fill(0, 0, 0)
     ellipse(moleX-10, moleY-15, 10, 10) # eyes
     ellipse(moleX+10, moleY-15, 10, 10)
     ellipse(moleX, moleY-5, 10, 10) # nose
     ellipse(moleX, moleY+10, 20, 5) # mouth
