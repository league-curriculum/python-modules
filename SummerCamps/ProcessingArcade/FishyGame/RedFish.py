from Fish import Fish

class RedFish(Fish):
    still_image_l = still_image_r = scared_image_l = scared_image_r = None
    images_l = list()
    images_r = list()
    num_images = 20
    image_width = 121
    image_height = 99
    type = 'fish'
    images_initialized = False
    
    @staticmethod
    def initialize_images():
#        if RedFish.images_initialized:
#            return
                        
        Fish.load_images(RedFish.type, RedFish.images_l, RedFish.images_r,
                         RedFish.num_images, RedFish.image_width, RedFish.image_height)
        Fish.resize_images(RedFish.images_l, RedFish.image_width, RedFish.image_height)
        Fish.resize_images(RedFish.images_r, RedFish.image_width, RedFish.image_height)
        
        RedFish.still_image_l = RedFish.images_l[0]
        RedFish.still_image_r = RedFish.images_r[0]
        RedFish.scared_image_l = loadImage("scared_fish_L.png")
        RedFish.scared_image_l.resize(RedFish.image_width, RedFish.image_height)
        RedFish.scared_image_r = loadImage("scared_fish_R.png")
        RedFish.scared_image_r.resize(RedFish.image_width, RedFish.image_height)
        images_initialized = True
        
    def __init__(self, x, y):
        Fish.__init__(self, RedFish.type, x, y)
        
        self.num_images = RedFish.num_images
        self.images_left = RedFish.images_l
        self.images_right = RedFish.images_r
        self.still_img_l = RedFish.still_image_l
        self.still_img_r = RedFish.still_image_r
        self.width = RedFish.image_width
        self.height = RedFish.image_height
        
    def end(self):
        if self.direction == 'right':
            image(RedFish.scared_fish_r, self.x, self.y)
        elif self.direction == 'left':
            image(RedFish.scared_fish_l, self.x, self.y)
        
