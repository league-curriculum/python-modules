class Rain:
    MAX_RAIN_DROPS = 1000
     
    # Default rain color is light blue
    def __init__(self, rain_color='#ADD8E6'):
       self.amount_of_rain = 100
       self.rain_color = rain_color
       self.drop = list()
       self.splash = list()
       self.initialized = False

    def set_amount_of_rain(self, rain):
        if rain > 0 and rain < Rain.MAX_RAIN_DROPS:
            self.amount_of_rain = rain

    def setup(self):
        for i in range(Rain.MAX_RAIN_DROPS):
            self.drop.append(Raindrop())
        
        initialized = True

    def draw(self):
        push()

        if not self.initialized:
            self.setup()

        stroke(255, 200)
        strokeWeight(1.8)

        for i in range(self.amount_of_rain):
            self.drop[i].draw(self.rain_color)
            self.drop[i].fall()
            
            if self.drop[i].y >= height:
                self.splash.append( Splash( self.drop[i].x) )
                self.drop[i].reset()

        for s in self.splash:
            s.fade()
            s.draw(self.rain_color);

        self.splash[:] = [sp for sp in self.splash if not sp.over()]
            
        pop()


class Raindrop:
    def __init__(self):
        self.x = random(-300, width + 300)
        self.y = random(-1400, -200)
        self.l = 30 + random(-10, 10)
        self.speed = 0
        self.angle = 0
        self.g = 0.14

    def draw(self, rain_color):
      stroke(rain_color)
      line(self.x, self.y, self.x + (self.l * sin(self.angle)), self.y + (self.l * cos(self.angle)))

    def fall(self):
      self.angle = map(mouseX - 300, -300, 300, -PI / 12, PI / 12)
      self.y += self.speed * cos(self.angle)
      self.x += self.speed * sin(self.angle)
      self.speed += self.g

    def reset(self):
      self.x = random(-300, width + 300)
      self.y = random(-800, -200)
      self.speed = 11


class Splash:
    def __init__(self, x):
      self.x = x
      self.a = 0
      self.b = 0
      self.l = 5 + random(13)
      self.offset = random(5)

    def draw(self, rain_color):
      stroke(rain_color)
      line(self.x - self.a, height - self.offset - self.a, self.x - self.b, height - self.offset - self.b)
      line(self.x + self.a, height - self.offset - self.a, self.x + self.b, height - self.offset - self.b)

    def fade(self):
        if self.b < self.l:
            self.b += 4
        elif self.a < self.l:
            self.a += 4

    def over(self):
      if self.a >= self.l and self.b >= self.l:
        return True
      else:
        return False
