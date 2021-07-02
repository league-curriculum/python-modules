from Fish import Fish
from RedFish import RedFish
from FriendlyFish import FriendlyFish
from Shark import Shark
from Anchovy import Anchovy

def setup():
    # 1. Use the fullScreen() function to make the game window the entire screen
    fullScreen()
 
    global bg, fish, sharks, anchovies
    
    # 2. Initialize the 'bg' variable with one of the four underwater backgrounds
    #    bg = loadImage("underwater_bg1.jpg")
    #    bg = loadImage("underwater_bg2.jpg")
    #    bg = loadImage("underwater_bg3.jpg")
    #    bg = loadImage("underwater_bg4.jpg")
    bg = loadImage("underwater_bg1.jpg")
    
    # 3. Use bg's resize(wdith, height) method to set the background to the entire screen
    bg.resize(width, height)

    # 4. Initialize the 'fish' variable using the create_red_fish(x, y) function
    #    fish = create_red_fish(width/2, height/2) # places the fish in the center of the window 
    fish = create_red_fish(width/2, height/2)
    
    # 5. Initialize the 'sharks' variable using the create_sharks() function
    sharks = create_sharks()
    
    # 6. Initialize the 'anchovies' variable using the create_anchovies() function
    anchovies = create_anchovies()

    setup_game()

def draw():
    global fish, sharks, anchovies, anchovies_eaten
    if display_intro():
        return

    # 7. Use the background() function to draw the bg image 
    # Do you see the game's background image?
    background(bg)

    # 8. Use the fish variable's draw() method to draw the fish
    # Do you see the red fish on the screen?
    fish.draw()
    
    #
    # 9. Skip below to the mouseDragged() function below to make the fish move
    #
    
    # 12. Use the spawn_sharks() function to create sharks
    spawn_sharks()
    
    # 13. Use the move_sharks() function to move the sharks
    # The sharks won't appear yet. They have to drawn first.
    move_sharks()

    # 14. Use a for loop through all the sharks in the 'sharks' list 
    for shark in sharks:
    
        # 15. Call the draw() method for each shark
        # Do you see the sharks?
        # The sharks won't interact with the fish until the collision is checked 
        shark.draw()
        
        # 16. Use an if statement and the is_collision(fish, shark) function to check for a collision
        # *HINT* the is_collision() function returns a boolean value
        if is_collision(fish, shark):
            
            # 17. If there is a collision, use the text("message", x, y) function to print "GAME OVER"
            #     Use textSize() and fill() before text() to set the color and size of the message
            textSize(90)
            fill(0)
            text("Game Over", width/3, height/2)
            
            # 18. Use noLoop() to stop the game
            # Does the game stop when the fish collides with the shark?
            noLoop()

    # 19. Use the spawn_anchovies() function to create anchovies
    spawn_anchovies()
    
    # 20. Use the move_anchovies() function to move the anchovies
    # The anchovies won't appear yet. They have to drawn first.
    move_anchovies()
    
    # 21. Use a for loop through all the anchovies in the 'anchovies' list
    for anchovy in anchovies:
        
        # 22. Call the draw() method for each anchovy
        # Do you see the small, green anchovies?
        anchovy.draw()
    
        # 23. Use an if statement and the is_collision(fish, anchovy) function to check for a collision
        # *HINT* the is_collision() function returns a boolean value
        if is_collision(fish, anchovy):
            
            # 24. If there is a collision, set anchovy.is_alive to False
            # Do the anchovies disappear when the fish collides with them?
            anchovy.is_alive = False
            
            # 25. If there is a collision, increase 'anchovies_eaten' by 1 
            anchovies_eaten += 1
    
    # 26. Use the text("message", x, y) function to print the anchovies_eaten variable on the game window
    #     Use textSize() and fill() before text() to set the color and size of the message
    textSize(48)
    fill(0)
    text("Anchovies Eaten: ", 20, 50)
    fill(255, 255, 0)
    text(str(anchovies_eaten), 450, 50)

def mouseDragged():
    pass
    # 10. Use the fish variable's follow_mouse() method to move the fish
    # Does the fish move when you click on it and drag the mouse across the screen?
    # The fish won't stop moving until we finish the code in the mouseReleased() function
    fish.follow_mouse()
        
def mouseReleased():
    pass
    # 11. Use the fish variable's stop() method to stop moving the fish when no longer pressing the mouse
    # Does the fish stop moving when the mouse is released?
    # If so, go back up and finish the code in the draw() function
    fish.stop()
    
    
    
    
# =================== DO NOT MODIFY THE CODE BELOW ======================
    
def keyPressed():
    if key == ENTER:
        global fish, sharks, anchovies, anchovies_eaten
        anchovies_eaten = 0
        fish = create_red_fish(width/2, height/2)
        sharks = create_sharks()
        anchovies = create_anchovies()
        loop()
    elif key == 's':
        global started
        started = True
    elif key == 'e':
        global anchovies_eaten
        anchovies_eaten += 1

def display_intro():
    if bg is not None and not started:
        background(bg)
        filter(BLUR, 6)
        image(title, width/2, height/4)
        textSize(90)
        fill(0)
        text("Press 's' to start", width/3, height/2)
        textSize(36)
        text("Click and drag the mouse to move\nthe red fish and avoid the sharks", (width/3) + 50, (height/2) + 100)    
        return True
    return False

def setup_game():
    frameRate(30)
    imageMode(CENTER)
    global title, started, shark_timer, anchovy_timer, anchovies_eaten
    title = loadImage("title.png")
    title.resize(width/2, height/4)
    started = False
    anchovies_eaten = 0
    shark_timer = anchovy_timer = millis();

def create_red_fish(x, y):
    RedFish.initialize_images()
    fish = RedFish(x, y)
    return fish

def create_sharks():
    Shark.initialize_images()
    return list()

def create_anchovies():
    Anchovy.initialize_images()
    return list()

def create_shark():
    new_x = -100 if random(100) < 50.0 else width + 100
    new_y = int(random(50, height - 100))
    new_shark = Shark(new_x, new_y)
    new_shark.direction = 'right' if new_x < 0 else 'left'
    
    if anchovies_eaten >= 5 and anchovies_eaten < 10 :
        new_shark.speed = int(random(15, 25))
    elif anchovies_eaten >= 10 and anchovies_eaten < 15 :
        new_shark.speed = int(random(25, 35))
    elif anchovies_eaten >= 15 and anchovies_eaten < 20 :
        new_shark.speed = int(random(35, 50))
    elif anchovies_eaten >= 20 and anchovies_eaten < 25 :
        new_shark.speed = int(random(50, 65))
    elif anchovies_eaten >= 25:
        new_shark.speed = int(random(65, 80))

    sharks.append(new_shark)

def move_sharks():
    global sharks
    
    for shark in sharks:
        if shark.direction == 'right':
            shark.move_right()
        elif shark.direction == 'left':
            shark.move_left()
            
    sharks[:] = [shark for shark in sharks if shark.is_alive]

def spawn_sharks():
    global shark_timer
    
    spawn_interval_ms = 500
    
    if millis() - shark_timer > spawn_interval_ms :
        if len(sharks) == 0:
            create_shark()
        elif len(sharks) < 3:
            if random(100) < 90.0:
                create_shark()
        elif len(sharks) < 6:
            if random(100) < 60.0:
                create_shark()
                
        shark_timer = millis()

def create_anchovy():
    new_x = -Anchovy.image_width/2 if random(100) < 50.0 else width + Anchovy.image_width/2
    new_y = int(random(50, height - 100))
    new_anchovy = Anchovy(new_x, new_y)
    new_anchovy.direction = 'right' if new_x < 0 else 'left'
    
    if anchovies_eaten >= 5 and anchovies_eaten < 10 :
        new_anchovy.speed = int(random(10, 20))
    elif anchovies_eaten >= 10 and anchovies_eaten < 15 :
        new_anchovy.speed = int(random(20, 30))
    elif anchovies_eaten >= 15 and anchovies_eaten < 20 :
        new_anchovy.speed = int(random(30, 40))
    elif anchovies_eaten >= 20 and anchovies_eaten < 25 :
        new_anchovy.speed = int(random(40, 50))
    elif anchovies_eaten > 30:
        new_anchovy.speed = int(random(50, 60))
    
    anchovies.append(new_anchovy)

def move_anchovies():
    global anchovies
    
    for anchovy in anchovies:
        if anchovy.direction == 'right':
            anchovy.move_right()
        elif anchovy.direction == 'left':
            anchovy.move_left()

    anchovies[:] = [anchovy for anchovy in anchovies if anchovy.is_alive]

def spawn_anchovies():
    global anchovy_timer
    
    spawn_interval_ms = 1000
    
    if millis() - anchovy_timer > spawn_interval_ms :
        if len(anchovies) == 0:
            create_anchovy()
        elif len(anchovies) < 6:
            if random(100) < 70.0:
                create_anchovy()
        elif len(anchovies) < 10:
            if random(100) < 30.0:
                create_anchovy()
                
        anchovy_timer = millis()

def is_collision(fish_1, fish_2):
    if fish_1 is None or fish_2 is None:
        return False
    
    r1x = fish_1.x - ((3*fish_1.width) / 8)
    r2x = fish_2.x - ((3*fish_2.width) / 8)
    r1y = fish_1.y - ((2*fish_1.height) / 8)
    r2y = fish_2.y - ((2*fish_2.height) / 8)
    r1w = (6*fish_1.width) / 8
    r2w = (6*fish_2.width) / 8
    r1h = (5*fish_1.height) / 8
    r2h = (5*fish_2.height) / 8
    
    # Uncomment to see collision boxes
    #noFill()
    #rect( r1x, r1y, r1w, r1h )
    #rect( r2x, r2y, r2w, r2h )
    
    if (r1x + r1w >= r2x and
        r1x <= r2x + r2w and
        r1y + r1h >= r2y and
        r1y <= r2y + r2h):
        return True
    
    return False

    
