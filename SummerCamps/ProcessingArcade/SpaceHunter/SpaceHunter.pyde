# background image: https://www.freepik.com/free-photos-vectors/star created by upklyak
from Alien import Alien
from EnergyBar import EnergyBar
from Shot import Shot

def setup():
    # 1. Use the fullScreen() function to make the game window the entire screen
    fullScreen();
    
    global bg, aliens, shots, energy_bar, crosshair
    
    # 2. Initialize the 'bg' variable for the background image
    #    bg = loadImage("spaceBg.png")
    bg = loadImage("spaceBg.png")
    
    # 3. Use the bg variable's resize(width, height) method to set the background
    # to the entire screen
    # Do you see the start screen with the blurred background image?
    bg.resize(width, height)
    
    # 5. Initialize the 'energy_bar' variable to an EnergyBar()
    # energy_bar = EnergyBar()
    energy_bar = EnergyBar()
    
    # 6. Initialize the 'shots' variable to a list()
    shots = list()
    
    # 7. UInitialize the 'crosshair' variable for the crosshair image
    #    crosshair = loadImage("crosshair1.png") 
    crosshair = loadImage("crosshair2.png")
    
    # 8. Use the crosshair's resize(width, height) method to resize
    # the crosshair to 150, 150 (or whatever size you want it)
    crosshair.resize(150, 150)

    # 9. Initialize the 'aliens' variable using the create_aliens() function
    aliens = create_aliens()

    
    setup_game()

def draw():
    global score
    if display_intro():
        return
    
    # 10. Use the image(bg, width/2, heigh/2) function to display the background
    # Do you see the background when you run the code?
    image(bg, width/2, height/2)
    
    # 11. Use the energy_bar's draw() method to display it on the game
    # Do you see the energy bar on the screen?
    energy_bar.draw()
    
    # 12. Call the spawn_aliens() function to generate aliens
    # The aliens don't appear yet! Do the next steps to move and draw them.
    spawn_aliens()
    
    # 13. Use a for loop to iterate though all the aliens
    for alien in aliens:
        
        # 14. Call the move() method for each alien
        alien.move()
        
        # 15. Call the draw() method for each alien
        # Do you see the aliens?
        alien.draw()        
    
    # 16. Use the image(crosshair, mouseX, mouseY) function to draw
    # the crosshair. Do you see it on the game when you run the code?
    image(crosshair, mouseX, mouseY)
    
    # 17. Next is coding the shot when the mouse is pressed.
    # Use an if statement to check the 'mousePressed' variable
    if mousePressed:
        
        # 18. Call the fire_shot() function to shoot
        # The shot won't appear, but it will drain the energy
        # The shots are drawn on the next step
        fire_shot()
    
    # 19. Use a for loop to iterate through all the shots
    for shot in shots:
        
        # 20. Call the draw() method for each shot
        # Do you see the shot when the mouse is clicked?
        shot.draw()
        
        # 21. Now let's check if we shot one of the aliens
        # Use a for loop to iterate through all the aliens
        for alien in aliens:
            
            # 22. Use an if statement and the is_collision(shot, alien) function
            # to check if an alien was shot
            if is_collision(shot, alien):
                
                # 23. If the alien was shot, set the alien's 'is_alive' variable to False
                # The alien won't disapear yet, that's handled later
                alien.is_alive = False
                
                # 24. Increase score by 1
                # The score will be draw later so it won't appear on the game yet
                score += 1
    
    # 25. Call the purge_objects() function to remove aliens and other objects from the game
    # Do you see the aliens disappear when they're shot?
    purge_objects()
    
    # 26. Use the text(str(score), x, y) function to print the 'score' variable
    # on the screen somewhere
    #   Use textSize() and fill() before text() to set the color and size of the message
    fill(0)
    textSize(64)
    text(str(score), 100, 100)

    # 27. Call the update_timer() function to count down the game's time
    # Do you see the game time counting down?
    update_timer()

    
    
# =================== DO NOT MODIFY THE CODE BELOW ======================

def keyPressed():
    if key == ENTER:
        setup_game()
        loop()
    elif key == 's':
        global started
        started = True

def mouseReleased():
    global total_shots
    total_shots += 1

def display_intro():
    if not started:
        image(bg, width/2, height/2)
        filter(BLUR, 6)
        image(title, width/2, height/4)
        textSize(90)
        fill(0)
        text("Press 's' to start", width/3, height/2)
        textSize(36)
        intro  = "Click the mouse to shoot as many\n"
        intro += "          UFOs in " + str(time_remaining) + " seconds"
        text(intro, (width/3) + 50, (height/2) + 100)    
        return True
    return False

def setup_game():
    imageMode(CENTER)
    noCursor()
    
    global title, started, total_shots, score
    global time_remaining, game_timer, alien_timer
    title = loadImage('title.png')
    started = False
    total_shots = 0
    score = 0
    time_remaining = 30
    game_timer = alien_timer = millis()
    
def end_game():
    noLoop()
    
    push()
    filter(BLUR, 6)
    textSize(90)
    fill(0)
    text("GAME OVER", width/3, height/2)
    textSize(36)
    intro  = "UFOs shot:   " + str(score) + "\n"
    intro += "total shots: " + str(total_shots) + "\n"
    intro += "accuracy:    "
    if total_shots == 0:
        intro += "0.0"
    else:
        intro += str(100.0 * float(score) / float(total_shots)) + '%'
    text(intro, (width/3) + 100, (height/2) + 100)
    text("press ENTER to restart", (width/3) + 100, (height/2) + 275)
    pop()
    
def update_timer():
    global game_timer, time_remaining
    
    if millis() - game_timer > 1000:
        time_remaining -= 1    
        game_timer = millis()
        
    push()
    textSize(128)
    if time_remaining < 10:
        fill(255, 0, 0)
    else:
        fill(0)
    text(str(time_remaining), (width/2) - 100, 200)
    pop()
    
    if time_remaining == 0:
        end_game()
    
def create_aliens():
    Alien.initialize_images()
    return list()

def create_alien():
    new_alien = Alien( speed=int(random(5, 15)) )
    aliens.append(new_alien)

def spawn_aliens():
    global alien_timer
    
    spawn_interval_ms = 500
    
    if millis() - alien_timer > spawn_interval_ms:
        if len(aliens) == 0:
            create_alien()
        elif len(aliens) < 3:
            if random(100) < 90.0:
                create_alien()
        elif len(aliens) < 6:
            if random(100) < 60.0:
                create_alien()
    
        alien_timer = millis()

def purge_objects():
    if len(aliens) > 0:
        aliens[:] = [alien for alien in aliens if alien.is_alive]
        
    if len(shots) > 0:
        shots[:] = [shot for shot in shots if shot.is_alive]

def fire_shot():
    if energy_bar.is_enough_energy_for_shot():
        # Flashes
        #filter(INVERT)
        
        shots.append(Shot())
        energy_bar.shot_fired()
        
        # total_shots is incremented in mouseReleased()
        # because it had more accurate counts


def is_collision(shot, alien):
    c1x = shot.x
    c1y = shot.y
    c1r = Shot.collision_radius
    c2x = alien.x
    c2y = alien.y
    c2r = Alien.collision_radius
    dist_x = c1x - c2x
    dist_y = c1y - c2y
    distance = sqrt( (dist_x * dist_x) + (dist_y * dist_y) )
    
    return distance <= (c1r + c2r)
