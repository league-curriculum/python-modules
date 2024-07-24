class Lightning:
    
    def __init__(self):
        self.chaos = 0.25
        self.points = list()
        self.flash = False

    def set_lightning_flash(self, on_off=True):
        self.flash = on_off

    # Draw lightning at random times.
    #   smaller input = more frequent lightning
    #   larger input  = less frequent lightning
    def draw(self, rand_delay=None):
        if rand_delay is None:
            self.draw_lightning()
        elif random(rand_delay) < 5:
            self.draw_lightning()

        if self.flash:
            filter(INVERT)

    def draw_lightning(self):
        push()
        noStroke()
    
        p1 = PVector(random(width), 0)
        p2 = PVector(random(width), height)

        self.points = self.chaotic_points(p1.x, p1.y, p2.x, p2.y, self.chaos)
        self.points.append(p2)

        stroke(64, 46, 255, 32)
        strokeWeight(32)
        self.draw_chaotic_line(self.points)

        stroke(64, 64, 255, 32)
        strokeWeight(16)
        self.draw_chaotic_line(self.points)

        stroke(128, 128, 255, 32)
        strokeWeight(8)
        self.draw_chaotic_line(self.points)

        stroke(255, 255, 255, 255)
        strokeWeight(4)
        self.draw_chaotic_line(self.points)

        pop()

    def chaotic_points(self, x1, y1, x2, y2, chaos):
        ptlist = list()  
        d_x = x2-x1
        d_y = y2-y1
        mag = sqrt(d_x*d_x + d_y*d_y)
    
        if mag > 10:
            ch = randomGaussian() * self.chaos / 2.0;

            # Take a random point on the line perpendicular to the given segment and 
            # passing through the midpoint of the segment
            xc = ((x1+x2) / 2) - d_y*ch
            yc = ((y1+y2) / 2) + d_x*ch
            ptlist += self.chaotic_points(x1, y1, xc, yc, self.chaos)
            ptlist += self.chaotic_points(xc, yc, x2, y2, self.chaos)
            return ptlist
        else:
            line(x1, y1, x2, y2)
            ptlist.append(PVector(x1, y1))
            return ptlist


    def draw_chaotic_line(self, points):
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            line(p1.x, p1.y, p2.x, p2.y)
