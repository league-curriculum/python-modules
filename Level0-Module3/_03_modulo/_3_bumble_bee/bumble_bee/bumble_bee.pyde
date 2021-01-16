def setup():
     ellipseMode(CENTER)
     size(500, 500)
     background(160, 160, 160)
     draw_flower(350, 100)


def draw():
    
    # First run the program and you should see a flower.  
  
  
    # Then, use a loop to make a body for the Bee! 
    # (see the image on the recipe, it's a diagonal line of circles)
    # Use modulo to make the colors alternate between yellow and black
    



    # Now put his head on using draw_bee_face(x,y)
    

    pass

#**************   Use these methods but  DON'T CHANGE THE CODE BELOW  **************/

def draw_flower(x, y):
     noStroke()
     translate(x, y)
     # draw 5 petals, rotating after each one
     fill(176,255,152)      # green
     for i in range(5):
        ellipse(0, -40, 50, 50)
        rotate(radians(72))
          
     fill(252,255,167) # light yellow
     ellipse(0, 0, 50, 50)

def draw_bee_face(bee_face_x, bee_face_y):
     noStroke()
     fill(0, 0, 0)
     stroke(1)
     strokeWeight(5)
     line(bee_face_x-10, bee_face_y-27, bee_face_x-17, bee_face_y-50)
     line(bee_face_x+10, bee_face_y-27, bee_face_x+17, bee_face_y-50)
     ellipse(bee_face_x-17, bee_face_y-50, 10, 10)
     ellipse(bee_face_x+17, bee_face_y-50, 10, 10)
     noStroke()
     fill(255, 251, 28)
     ellipse(bee_face_x, bee_face_y, 60, 60) # face
     fill(255, 237, 209)
     fill(0,0,0)
     ellipse(bee_face_x-10, bee_face_y-15, 10, 10) # eyes
     ellipse(bee_face_x+10, bee_face_y-15, 10, 10)
     ellipse(bee_face_x, bee_face_y-5, 10, 10) # nose
     ellipse(bee_face_x, bee_face_y+10, 20, 10) # mouth
     fill(255, 251, 28)
     ellipse(bee_face_x, bee_face_y+5, 20, 6)
