bird_x = 50
bird_y = 200
bird_width = 50
bird_height = 3 * bird_width / 4
bird_y_velocity = 15
gravity = 3
pipe_gap = 4 * bird_height

def setup():
    size(500, 500)
    
    global flappy_bird, lower_pipe, upper_pipe, bg
    flappy_bird = loadImage("bird.png")
    flappy_bird.resize(bird_width, bird_height)
    upper_pipe = Pipe("topPipe.png")
    lower_pipe = Pipe("bottomPipe.png")
    reset_pipes()
    bg = loadImage("flappyBackground.jpg")
    bg.resize(width, height)

def draw():
    global bird_y
    background(bg)
    
    image(flappy_bird, bird_x, bird_y)    
    bird_y += gravity
    
    if mousePressed:
        bird_y -= bird_y_velocity
    
    upper_pipe.update()
    lower_pipe.update()
                
    upper_pipe.draw()
    lower_pipe.draw()
    
    if intersects_pipes():
        noLoop()
    
    if upper_pipe.x < -upper_pipe.width:
        reset_pipes()

class Pipe:
    def __init__(self, image_file, pipe_y=0, pipe_height=0):
        self.x = width
        self.y = pipe_y
        self.width = 50
        self.height = pipe_height
        self.image = loadImage(image_file)
        self.image.resize(self.width, self.height)
    
    def update(self):
        self.x -= 3
    
    def draw(self):
        image(self.image, self.x, self.y)

    def teleport(self, pipe_y, pipe_height):
        self.x = width
        self.y = pipe_y
        self.height = pipe_height
        self.image.resize(self.width, self.height)

def reset_pipes():
    random_height = int((2 * random(height) / 3) + 50)
    upper_pipe.teleport(0, random_height)
    lower_pipe.teleport(random_height + pipe_gap, height - random_height)
    
def intersects_pipes():
  if (bird_x + bird_width >= upper_pipe.x and
      bird_x <= upper_pipe.x + upper_pipe.width and
      bird_y + bird_height >= upper_pipe.y and
      bird_y <= upper_pipe.y + upper_pipe.height):
    return True

  if (bird_x + bird_width >= lower_pipe.x and
      bird_x <= lower_pipe.x + lower_pipe.width and
      bird_y + bird_height >= lower_pipe.y and
      bird_y <= lower_pipe.y + lower_pipe.height):
    return True

  if bird_y > height or bird_y + bird_height < 0:
    return True

  return False
