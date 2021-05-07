"""
Create a single player Pong game
"""
from Ball import Ball
from Paddle import Paddle
global started
started = False

def setup():
    pass
    # 1. Set the size of your window to at least width = 800, height = 600

    # 2. Make a global ball variable, for example:
    
    # 3. Initialize your ball variable to a new Ball(), for example:
    
    # 4. Make a global paddle variable.
    
    # 5. Initialize your paddle variable to a new Paddle() for example:
    
def draw():
    if not started:
        textSize(32)
        fill(0)
        text("Press 's' to start", width/3, height/2)
        return
    
    # 6. Use the background() function to set the background color.
    #    background(0) will set a classic black background

    # 7. Call the ball object's update() and draw() methods.
    #    Do you see the ball moving on the screen?

    # 8. Call the paddle object's update() and draw() methods.
    #    Do you see the paddle on the screen?

    # 11. Finish the code in keyPressed() and keyReleased() first!
    #     Call the ball object's collision() method and pass the
    #     paddle object as an input variable.
    #     Does the ball bounce off the paddel?

    # 12. End the game when the ball goes below the bottom of the screen.
    #     You can use noLoop() to freeze the game and text() to print text
    #     on the screen.

    # 13. Figure out how to add a score to the game so every bounce off
    #     the paddle increases the player socre

    # *EXTRA*
    # Can you figure out how to make a 2 player pong game with paddles on
    # the left and right on the screen?
    
    pass

# 9. Change paddle.x_speed when the LEFT or RIGHT arrow keys are pressed.
#    Does the paddle move?
def keyPressed():
    if key == 's':
        global started
        started = True 
    elif key == CODED:
        if keyCode == LEFT:
            
            pass


# 10. Set paddle.x_speed to 0 when the LEFT or RIGHT arrow keys are released.
#     Does the paddle stop when the keys are released?
def keyReleased():
    if key == CODED:
        pass
