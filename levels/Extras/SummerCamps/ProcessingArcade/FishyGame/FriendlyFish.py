from Fish import Fish

class FriendlyFish(Fish):
    still_image_l = still_image_r = None
    images_l = list()
    images_r = list()
    num_images = 12
    image_width = 120
    image_height = 71
    type = 'fish_friend'
    images_initialized = False
    
    @staticmethod
    def initialize_images():
        if FriendlyFish.images_initialized:
            return
        
        Fish.load_images(FriendlyFish.type, FriendlyFish.images_l, FriendlyFish.images_r,
                         FriendlyFish.num_images, FriendlyFish.image_width, FriendlyFish.image_height)
        Fish.resize_images(FriendlyFish.images_l, FriendlyFish.image_width, FriendlyFish.image_height)
        Fish.resize_images(FriendlyFish.images_r, FriendlyFish.image_width, FriendlyFish.image_height)
        
        FriendlyFish.still_image_l = FriendlyFish.images_l[0]
        FriendlyFish.still_image_r = FriendlyFish.images_r[0]
        images_initialized = True
        
    def __init__(self, x, y):
        Fish.__init__(self, FriendlyFish.type, x, y)
        
        self.num_images = FriendlyFish.num_images
        self.images_left = FriendlyFish.images_l
        self.images_right = FriendlyFish.images_r
        self.still_img_l = FriendlyFish.still_image_l
        self.still_img_r = FriendlyFish.still_image_r
        self.width = FriendlyFish.image_width
        self.height = FriendlyFish.image_height
        self.move_state = Fish.MOVE_CONSTANT
        
