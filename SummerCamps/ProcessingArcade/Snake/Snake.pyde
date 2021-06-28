from Segment import Segment
from Food import Food

# All the game variables that will be shared by the game methods are here
global food, direction, snake_head, snake_body
food_eaten = 0
food = None
direction = None
snake_head = None
snake_body = list()

#
# ***** START HERE *****
# First steps are to create the program window, snake head, and food
#
def setup():
    global snake_head, food
    frameRate(15 + food_eaten)
    
    # 1. Use size(width, height) to set the width and height of the window
    #size(800, 600
    
    # 2. Initialize the 'snake_head' variable using the Segment class to a new snake segment.
    #snake_head = Segment(x, y)
    
    # 3. Initialize the 'food' variable using the Food class to make new food
    
    # 4. Use the food's drop() method to place a peice of food randomly in the window.


def draw():
    global food_eaten
    
    # 5. Use the background(color) function to draw the game background
    # Example: background(0)    # black background 
    
    # 6. Use the draw_snake() function to display the snake
    # Do you see the snake on the window?
    
    # 7. Use the move_snake() function to move the snake
    # Do the UP, DOWN. LEFT, RIGHT arrow keys move the snake? 
    
    # 8. Use the check_tail_collision() function to check if the head
    # has collided with the body (when the tail gets really long)
    
    # 9. Use the food's draw() method to display the food
    # Do you see the green food?
    
    # 10. Use an if statement and the collision() function check if the
    # snake_head variable collides with the food variable
        
        # 11. If there is a collision, increase the food_eaten variable by 1
        
        # 12. If there is a collision, call the food variable's drop method
        
        # 13. Use the Segment(snake_head.x, snake_head.y) class to make a
        # new snake segment and save it to a variable
        
        # 14. Call the snake_body variable's append() method to add the new
        # snake segment

    
    # 15. Use the text("message", x, y) function to display the number of food
    # eaten using the 'food_eaten' variable.
    
    
    # *** ENHANCEMENTS ***
    # * Changing the game background.
    # * Can you figure out how to change the color of each snake segment?
    #   Hint: use the Segment class' constructor
    # * Changing the food from a square to an image, like a pizza?
    # * Can you make the game faster the more food the snake eats?
    #   Hint: use the frameRate() function


# =================== DO NOT MODIFY THE CODE BELOW ======================

#
# Set the direction of the snake according to the arrow keys pressed
#
def keyPressed():
    global direction

    if key == CODED:
        if keyCode == UP and direction != DOWN:
            direction = UP
        elif keyCode == DOWN and direction != UP:
            direction = DOWN
        elif keyCode == LEFT and direction != RIGHT:
            direction = LEFT
        elif keyCode == RIGHT and direction != LEFT:
            direction = RIGHT

# 
# Draw the head of the snake followed by its tail
#
def draw_snake():
    global snake_head, snake_body
    
    snake_head.draw()
    
    for snake_segment in snake_body:
        snake_segment.draw()
        
    # After drawing the tail, add a new segment at the "start" of the tail and remove the one at the "end" 
    # This produces the illusion of the snake tail moving.
    if len(snake_body) > 0:
        snake_body.insert( 0, Segment(snake_head.x, snake_head.y) )
        snake_body = snake_body[ : len(snake_body) - 1 ] 

#
# Change the location of the Snake head based on the direction it is moving.
#
def move_snake():
    global direction, snake_head
  
    if direction == UP:
        snake_head.y -= snake_head.speed
         
    elif direction == DOWN:
        snake_head.y += snake_head.speed
         
    elif direction == LEFT:
        snake_head.x -= snake_head.speed
        
    elif direction == RIGHT:
        snake_head.x += snake_head.speed
        
    check_boundaries()

#
# If the snake leaves the frame, make it reappear on the other side
#
def check_boundaries():
    global snake_head
    
    if snake_head.x >= width:
        snake_head.x = 0
    elif snake_head.x <= -snake_head.size:
        snake_head.x = width
    elif snake_head.y >= height:
        snake_head.y = 0
    elif snake_head.y <= -snake_head.size:
        snake_head.y = height

#
# If the snake crosses its own tail, shrink the tail back to one segment
#
def check_tail_collision():
    global snake_head, snake_body, food_eaten
  
    is_collision = False
  
    for segment in snake_body:
        if segment.x == snake_head.x and segment.y == snake_head.y:
            is_collision = True
            break
  
    if is_collision:
        food_eaten = 0
        snake_body = list()

#
# Detect collision between 2 squares/rectangles
#
def collision(rect1, rect2):
    if (rect1.x + rect1.size >= rect2.x and
        rect1.x <= rect2.x + rect2.size and
        rect1.y + rect1.size >= rect2.y and
        rect1.y <= rect2.y + rect2.size):
        return True;
    
    return False;
