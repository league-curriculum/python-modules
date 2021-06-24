from Fish import Fish

class Anchovy(Fish):
    still_image_l = still_image_r = None
    images_l = list()
    images_r = list()
    num_images = 15
    image_width = 75
    image_height = 26
    type = 'green_anchovy'
    images_initialized = False
    
    @staticmethod
    def initialize_images():
        if Anchovy.images_initialized:
            return
        
        Fish.load_images(Anchovy.type, Anchovy.images_l, Anchovy.images_r,
                         Anchovy.num_images, Anchovy.image_width, Anchovy.image_height)
        Fish.resize_images(Anchovy.images_l, Anchovy.image_width, Anchovy.image_height)
        Fish.resize_images(Anchovy.images_r, Anchovy.image_width, Anchovy.image_height)
        
        Anchovy.still_image_l = Anchovy.images_l[0]
        Anchovy.still_image_r = Anchovy.images_r[0]
        images_initialized = True
        
    def __init__(self, x, y):
        Fish.__init__(self, Anchovy.type, x, y)
        
        self.num_images = Anchovy.num_images
        self.images_left = Anchovy.images_l
        self.images_right = Anchovy.images_r
        self.still_img_l = Anchovy.still_image_l
        self.still_img_r = Anchovy.still_image_r
        self.width = Anchovy.image_width
        self.height = Anchovy.image_height
        self.move_state = Fish.MOVE_CONSTANT
