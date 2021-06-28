class Fish:
    STILL = -1           # Non-moving object
    MOVE_BY_MOUSE = 1    # Move by mouse drag
    MOVE_CONSTANT = 2    # Move at a constant speed

    def __init__(self, fish_type, x, y):
        self.fish_type = fish_type
        self.images_left = self.images_right = self.num_images = None
        self.width = self.height = None
        self.x, self.y = (x, y)
        self.direction = 'left'
        self.speed = 10
        self.move_state = Fish.STILL
        self.is_alive = True

    def draw(self):
        if self.move_state == Fish.STILL:
            if self.direction == 'right':
                image(self.still_img_r, self.x, self.y)
            else:
                image(self.still_img_l, self.x, self.y)
        elif self.move_state == Fish.MOVE_BY_MOUSE:
            if mouseX > self.x and self.direction == 'left':
                self.direction = 'right'
            elif mouseX < self.x and self.direction == 'right':
                self.direction = 'left'
                
            if self.direction == 'right':
                image(self.images_right[frameCount % self.num_images], self.x, self.y)
            else:
                image(self.images_left[frameCount % self.num_images], self.x, self.y)
        elif self.move_state == Fish.MOVE_CONSTANT:
            if self.direction == 'right':
                image(self.images_right[frameCount % self.num_images], self.x, self.y)
            else:
                image(self.images_left[frameCount % self.num_images], self.x, self.y)
                
    def move_left(self):
        self.direction = 'left'
        self.x -= self.speed
        if self.x < 2 * -self.width:
            self.is_alive = False
            
    def move_right(self):
        self.direction = 'right'
        self.x += self.speed
        if self.x > width + (2 * self.width):
            self.is_alive = False
            
    def follow_mouse(self):
        # Only move if mouse is over fish
        if self.move_state == Fish.STILL:
            if (mouseX < self.x - (self.width/2) or mouseX > self.x + (self.width/2) or
                mouseY < self.y - (self.height/2) or mouseY > self.y + (self.height/2)):
                return
        
        if mouseX > self.x and self.direction == 'left':
            self.direction = 'right'
        elif mouseX < self.x and self.direction == 'right':
            self.direction = 'left'
        
        self.move_state = Fish.MOVE_BY_MOUSE
        self.x = mouseX
        self.y = mouseY
        
    def stop(self):
        self.move_state = Fish.STILL
        
    def grow(self):
        self.width  += int(self.width / 40)
        self.height += int(self.height / 40)
        
        Fish.resize_images(self.images_l, self.width, self.height)
        Fish.resize_images(self.images_r, self.width, self.height)

    def shrink(self):
        self.width  -= int(self.width / 2)
        self.height -= int(self.height / 2)
        
        Fish.resize_images(self.images_l, self.width, self.height)
        Fish.resize_images(self.images_r, self.width, self.height)

    @staticmethod
    def resize_images(images, w, h):
        for img in images:
            img.resize(w, h)
        
    @staticmethod
    def load_images(fish_type, images_left, images_right, num_images, w, h):
        for i in range(num_images):
            filename_l = fish_type + str(i) + '_L.png'
            img_l = loadImage(filename_l)
            img_l.resize(w, h)
            images_left.append(img_l)
            
            filename_r = fish_type + str(i) + '_R.png'
            img_r = loadImage(filename_r)
            img_r.resize(w, h)
            images_right.append(img_r)
