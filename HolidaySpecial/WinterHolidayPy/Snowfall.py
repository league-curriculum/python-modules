class Snowfall:
  
    def __init__(self):
        self.snowfall = list()
    
        self.snowLevel = 0
        self.minSnowSize = 1
        self.maxSnowSize = 10
        self.isWindy = False
        self.amountSnowFallen = 0
        self.snowColor = '#FFFFFF'
    
        # Initial snowfall
        for i in range(100):
            self.addSnow(i)

    # Add additional snow!
    def addSnow(self, id):
        x = random(width)
        y = random(0)
        size = random(self.minSnowSize, self.maxSnowSize);
        self.snowfall.append( Snow(x, y, id, size) )
  
    def draw(self):
        push()
    
        fill(self.snowColor)
    
        # Draw snow on ground
        ellipse(width/2, height, width, 80 + self.snowLevel)

        if self.amountSnowFallen != 0 and self.amountSnowFallen % 50 == 0 :
            self.snowLevel += 1
    
        # Draw snow particles
        for snow in self.snowfall:
            snow.draw(self.isWindy)
    
        # Remove snow at the bottom if necessary
        originalSnowfallSize = len( self.snowfall )                
        self.snowfall = [particle for particle in self.snowfall if particle.y < height]
        remainingSnowfallSize = len( self.snowfall )
        self.amountSnowFallen += remainingSnowfallSize - originalSnowfallSize
    
        if frameCount % 2 == 0 :
            self.addSnow(frameCount)

        pop()


class Snow:
    
    def __init__(self, x, y, id, size):
        self.x = x
        self.y = y
        self.id = id
        self.size = size

    def draw(self, isWindy):
        self.y += cos( ( (self.id * 25) - frameCount ) / 50) * 0.5 + 1

        if isWindy:
            self.x += sin( ( (self.id * 9) + frameCount ) / 50) * 2

        # Draw snow!
        noStroke()
        arc(self.x, self.y, self.size, self.size, 0, 7)
