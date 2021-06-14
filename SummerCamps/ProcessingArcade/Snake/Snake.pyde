from SnakeSegment import Segment
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
    # Example:
    size(800, 600)
    
    # 2. Use the Segment class to make a new snake_head in the middle of the window.
    # #Example:
    snake_head = Segment(width / 2, height / 2)
    
    # 3. Use the Food class to make new food
    food = Food()
    
    # 4. Use the food's drop() method to place a peice of food randomly in the window.
    food.drop()

#
# These methods are used to draw the snake and its food
# 
def draw():
    # 5. Use the background(color) function to draw the game background
    # Example: background(0)    # black background 
    background(0)
    
    # 6. Use the draw_snake() function to display the snake
    # Do you see the snake on the window?
    draw_snake()
    
    # 7. Use the move_snake() function to move the snake
    # Do the UP, DOWN. LEFT, RIGHT arrow keys move the snake? 
    move_snake()
    
    # 8. Use the check_tail_collision() function to check if the head
    # has collided with the body (when the tail gets really long)
    check_tail_collision()
    
    # 9. Use the draw_food() function to display the food
    # Do you see the green food?
    draw_food()
    
    # 10. Use the eat() function to grow the snake's tail if the snake eats the food
    # Does the game work?
    eat()
    
    # 11. Use the text("message", x, y) function to display the number of food
    # eaten using the global food_eaten variable.
    # global food_eaten
    
    
    # *** ENHANCEMENTS ***
    # * Changing the game background.
    # * Can you figure out how to change the color of each snake segment?
    #   Hint: use the Segment class' constructor
    # * Changing the food from a square to an image, like a pizza?
    # * Can you make the game faster the more food the snake eats?
    #   Hint: use the frameRate() function

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
# Draw food
#
def draw_food():
    global food
    food.draw()

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
# When the snake eats the food, its tail should grow and
# another should food appear
#
def eat():
    global snake_body, snake_head, food, food_eaten

    if collision(snake_head, food):
        food_eaten += 1
        food.drop()
        snake_body.append( Segment(snake_head.x, snake_head.y) )

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
