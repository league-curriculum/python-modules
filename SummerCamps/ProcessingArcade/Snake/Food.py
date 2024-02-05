class Food:
    size = 20
    
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def draw(self):
        fill("#00FF00")
        rect(self.x, self.y, self.size, self.size)
        
    def drop(self, snake_head=None, snake_body=None):
        while True:
            #food = Food( int(random(width / Food.size) * Food.size), int(random(height / Food.size) * Food.size) )
            self.x = int(random(width / Food.size) * Food.size)
            self.y = int(random(height / Food.size) * Food.size)
            
            if snake_head is not None:
                if collision( snake_head, food ):
                    continue
            
            if snake_body is not None:
                collision = False
                for segment in snake_body:
                    if collision( segment, food ):
                        no_collision = False
                        break

                if collision:
                    continue
            
            # No collision found, use values
            break
