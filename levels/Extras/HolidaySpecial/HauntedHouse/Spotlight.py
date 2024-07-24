class Spotlight:
    SPOTLIGHT_SIZE_PIXELS = 125
    
    def __init__(self):
        # Sets how pixelated the spotlight view is; 1 to 9
        # 1 = no pixelization
        # 9 = high pixelization (large pixels)
        self.pixel_size = 1
        self.pixel_list = list()

        # DMC double check this
        # Foreground darkness image
        self.darkness = createImage(width, height, RGB)
        self.darkness.loadPixels()
        for i in range(len(self.darkness.pixels)):
           self.darkness.pixels[i] = 0
        self.darkness.updatePixels()

        # Ellipse mask for spotlight through darkness with no pixel distortion
        self.spotlight_mask = createGraphics(width, height)

    def set_pixel_size(self, new_size):
        self.pixel_size = new_size
        
    def set_size(self, new_size):
        Spotlight.SPOTLIGHT_SIZE_PIXELS = new_size
        
    def get_size(self):
        return Spotlight.SPOTLIGHT_SIZE_PIXELS

    def initialize_pixels(self):
        for i in range(0, width, self.pixel_size):
            for j in range(0, height, self.pixel_size):
                c = get(i, j)
                self.pixel_list.append( Pixel(i, j, self.pixel_size, c) )

    def draw(self):
        push()

        if len(self.pixel_list) == 0:
            self.initialize_pixels()

        if self.pixel_size > 1:
            # If pixelating

            background(0)

            for pixel in self.pixel_list:
                pixel.draw()

            self.pixel_list.clear()
        
        else: 
            # Not pixelating, use a normal spotlight with no pixel distortion

            # Get current frame before draing darkness
            current_frame = get()
      
            image(self.darkness, 0, 0)

            self.spotlight_mask.beginDraw()

            # Erase previously drawn graphics
            self.spotlight_mask.background(0)
            self.spotlight_mask.noStroke()

            # Ellipse mask with fuzzy edges
            spotlight_width = 2 * Spotlight.SPOTLIGHT_SIZE_PIXELS
            for i in range(25):
                self.spotlight_mask.fill(0 + (i * 10))
                self.spotlight_mask.ellipse(mouseX, mouseY, spotlight_width - (i * 2), spotlight_width - (i * 2))

            self.spotlight_mask.endDraw()

            current_frame.mask(self.spotlight_mask)
            image(current_frame, 0, 0)

        pop()


class Pixel:
    def __init__(self, x, y, pixel_size, pixel_color):
      self.x = x
      self.y = y
      self.pixel_size = pixel_size
      self.pixel_color = pixel_color

    def draw(self):
        size_pixels = Spotlight.SPOTLIGHT_SIZE_PIXELS * Spotlight.SPOTLIGHT_SIZE_PIXELS

        if ((self.x - mouseX) * (self.x - mouseX)) + ((self.y - mouseY) * (self.y - mouseY)) <= size_pixels:
            xm = self.x + random(-1, 1)
            ym = self.y + random(-1, 1)

            if xm > width or xm < 0:
                xm = -xm
            
            if ym > height or ym < 0:
                ym = -ym

            fill(this.pixel_color)
            rect(xm, ym, pixel_size, pixel_size)
