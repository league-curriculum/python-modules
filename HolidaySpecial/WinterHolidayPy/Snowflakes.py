class Snowflakes:
    def __init__(self, enableSparkle=False):
        self.snowflakes = list()
        self.gravity = 1
        self.sparkleEnabled = enableSparkle
        
        self.addSnowflake()
  
    def addSnowflake(self):
        x = random(width)
        y = -60
        w = random(20, 60)
    
        flake = Snowflake( x, y, w, self.gravity )
        flake.sparkle = self.sparkleEnabled
    
        self.snowflakes.append( flake )
  
    def draw(self):
        # Make a new snowflake at a specified interval
        if frameCount % 140 == 0 :
            self.addSnowflake()
    
        # Draw all the snowflakes
        for flake in self.snowflakes:
            flake.draw()

        # Remove snowflakes at the bottom of the screen
        self.snowflakes = [flake for flake in self.snowflakes if flake.y < height]


class Snowflake:
    
    def __init__(self, x, y, w, gravity):
        self.x = x
        self.y = y
        self.w = w
        self.r = 0
        self.gravity = gravity
        self.sparkle = False
        
        self.snowflakeColors = [ '#FFFFFF', '#1F1FFF', '#DBDFE0' ]
        randomColorIndex = int( random( len(self.snowflakeColors) ) ) 
        self.snowflakeColor = self.snowflakeColors[ randomColorIndex ]

        self.fallSpeed = random(0.0, 1.0)
        self.rotateSpeedDegrees = random(0.0, 3.0)

    def draw(self):
        push()
    
        if self.sparkle:
            stroke(red(self.snowflakeColor) - random(50), green(self.snowflakeColor) - random(50), blue(self.snowflakeColor) - random(50))
        else:
            # White snowflake
            stroke( self.snowflakeColor )
    
        m = 16
        pDegrees = 360 / m
    
        for i in range(m):
            if i % 2 == 0:
                self.drawBranch(self.x, self.y, self.w, pDegrees * i)
            else:
                self.drawBranch(self.x, self.y, self.w * 0.7, pDegrees * i)
    
        self.y += self.gravity + self.fallSpeed
        self.r += self.rotateSpeedDegrees
    
        pop()

    def drawBranch(self, x, y, w, rDegrees):
        push()
    
        translate(x, y)
        rotate(radians(rDegrees + self.r))
        strokeWeight(3)
        line(0, 0, w, 0)
        line(w*0.5, 0, w*0.6, w*0.2)
        line(w*0.5, 0, w*0.6, w*-0.2)
        line(w*0.7, 0, w*0.8, w*0.2)
        line(w*0.7, 0, w*0.8, w*-0.2)
    
        pop()
