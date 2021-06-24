from Fish import Fish
from RedFish import RedFish
from FriendlyFish import FriendlyFish
from Shark import Shark
from Anchovy import Anchovy

def setup():
    fullScreen()

    global bg
    bg = loadImage("underwater_bg.jpg")
    bg.resize(width, height)

    global fish, friendly_fish, sharks, anchovies
    fish = create_red_fish(width/2, height/2)
    
    sharks = create_sharks()
    
    FriendlyFish.initialize_images()
    friendly_fish = FriendlyFish(100, 100)
    
    anchovies = create_anchovies()

    frameRate(30)
    imageMode(CENTER)
    global title, started, shark_timer, anchovy_timer, anchovies_eaten
    title = loadImage("title.png")
    title.resize(width/2, height/4)
    started = False
    anchovies_eaten = 0
    shark_timer = anchovy_timer = millis();

def draw():
    global fish, friendly_fish, sharks, anchovies, anchovies_eaten
    if not started:
        background(bg)
        filter(BLUR, 6)
        image(title, width/2, height/4)
        textSize(90)
        fill(0)
        text("Press 's' to start", width/3, height/2)
        textSize(36)
        text("Click and drag the mouse to move\nthe red fish and avoid the sharks", (width/3) + 50, (height/2) + 100)    
        return

    background(bg)

    fish.draw()
    
    spawn_sharks()
    move_sharks()

    for shark in sharks:
        shark.draw()

    spawn_anchovies()
    move_anchovies()
    
    for anchovy in anchovies:
        anchovy.draw()
    
    for anchovy in anchovies:
        if is_collision(fish, anchovy):
            anchovies_eaten += 1
            anchovy.is_alive = False

    for shark in sharks:
        if is_collision(fish, shark):
            textSize(90)
            fill(0)
            text("Game Over", width/3, height/2)
            noLoop()
            
    textSize(48)
    fill(0)
    text("Anchovies Eaten: ", 20, 50)
    fill(255, 255, 0)
    text(str(anchovies_eaten), 450, 50)
    println( 'anch: ' + str(len(anchovies)) + '; sharks: ' + str(len(sharks)) )

def mouseDragged():
    fish.follow_mouse()
        
def mouseReleased():
    fish.stop()
    
def keyPressed():
    if key == ENTER:
        global fish, friendly_fish, sharks, anchovies, anchovies_eaten
        anchovies_eaten = 0
        fish = create_red_fish(width/2, height/2)
        sharks = create_sharks()
        friendly_fish = FriendlyFish(100, 100)
        anchovies = create_anchovies()
        loop()
    elif key == 's':
        global started
        started = True
        
# =================== DO NOT MODIFY THE CODE BELOW ======================

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
    elif anchovies_eaten > 30:
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

    
