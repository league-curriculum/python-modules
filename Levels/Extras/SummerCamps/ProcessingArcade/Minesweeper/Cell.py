class Cell:
    cell_width = 40
    images = None
    empty = one = two = three = four = five = six = seven = eight = None
    mine_img = pin_img = won_img = lost_img = None
  
    def __init__(self, i, j, cell_color, game_panel_height):
        self.i = i                   # cell row #
        self.j = j                   # cell col #
        self.x = i * Cell.cell_width # cell x in pixels
        self.y = j * Cell.cell_width # cell y in pixels
        self.y += game_panel_height  # cell y adjustment
        self.cell_color = cell_color
        self.mine = False
        self.revealed = False
        self.pinned = False
        self.mines_around = 0
    
    @staticmethod
    def initialize_images():
        Cell.empty = loadImage("empty.png");
        Cell.one = loadImage("1.png");
        Cell.two = loadImage("2.png");
        Cell.three = loadImage("3.png");
        Cell.four = loadImage("4.png");
        Cell.five = loadImage("5.png");
        Cell.six = loadImage("6.png");
        Cell.seven = loadImage("7.png");
        Cell.eight = loadImage("8.png");
        Cell.mine_img = loadImage("bomb.png");
        Cell.pin_img = loadImage("flag.png");
        Cell.won_img = loadImage("sunglasses.png");
        Cell.lost_img = loadImage("cry.png");
    
        # Only add new images to the end of the array. The array index
        # is used to display the corresponding image for surrounding mines.
        Cell.images = [Cell.empty, Cell.one, Cell.two, Cell.three, Cell.four,
                       Cell.five, Cell.six, Cell.seven, Cell.eight,
                       Cell.mine_img, Cell.pin_img, Cell.won_img, Cell.lost_img]
        
        for img in Cell.images:
            img.resize(Cell.cell_width, Cell.cell_width);
        
        
    def draw(self):
        if self.revealed:
            if self.mine:
                image(Cell.mine_img, self.x, self.y)
            else:
                image(Cell.images[self.mines_around], self.x, self.y)
        else:
            fill(self.cell_color)
            rect(self.x, self.y, Cell.cell_width, Cell.cell_width)
      
        # Draw pin after cell background
        if self.pinned:
            image(Cell.pin_img, self.x, self.y)
    
        # Draw cell border at the end on top of the images
        # for clearer cell seperation
        stroke(0)
        strokeWeight(1)
        noFill()
        rect(self.x, self.y, Cell.cell_width, Cell.cell_width)
