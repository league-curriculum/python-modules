from Fish import Fish

class Shark(Fish):
    still_image_l = still_image_r = None
    images_l = list()
    images_r = list()
    num_images = 10
    image_width = 2 * 200
    image_height = 2 * 78
    type = 'shark'
    images_initialized = False
    
    @staticmethod
    def initialize_images():
        if Shark.images_initialized:
            return
        
        Fish.load_images(Shark.type, Shark.images_l, Shark.images_r,
                         Shark.num_images, Shark.image_width, Shark.image_height)
        Fish.resize_images(Shark.images_l, Shark.image_width, Shark.image_height)
        Fish.resize_images(Shark.images_r, Shark.image_width, Shark.image_height)
        
        Shark.still_image_l = Shark.images_l[0]
        Shark.still_image_r = Shark.images_r[0]
        images_initialized = True
        
    def __init__(self, x, y):
        Fish.__init__(self, Shark.type, x, y)
        
        self.num_images = Shark.num_images
        self.images_left = Shark.images_l
        self.images_right = Shark.images_r
        self.still_img_l = Shark.still_image_l
        self.still_img_r = Shark.still_image_r
        self.width = Shark.image_width
        self.height = Shark.image_height
        self.move_state = Fish.MOVE_CONSTANT
