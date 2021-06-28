from Button import Button
from Cell import Cell

# Game variables
global rows, cells, game_ready, game_in_progress, now_ms, game_time_sec
rows = None                  # same number of columns as rows
cells = None
start_button = None
game_ready = False
game_in_progress = False
game_time_sec = None
now_ms = None

#
# Game settings
#
global cell_width, header_height, num_of_mines, mines_flagged, cell_color
cell_width = 40              # in pixels
header_height = cell_width   # height of game info header
num_of_mines = 10            # number of mines in the game
mines_flagged = 0            # number of mines flagged
cell_color = '#C0C0C0'       # color of unrevealed cell

#
# *** START HERE ***
# First steps are to create the program window, cells, and mines
#
def setup():
    pass
    # 1. Use size(width, height) to set the width and height of the window
    #size(400, 440)
    
    # 2. Use the initialize_game_data() function to set up the game header
    #initialize_game_data()
    
    # 3. Use the initialize_cells() function to set up the playing grid cells
    
    # 4. Use the initialize_mines() function to randomly place the mines


def draw():
    pass
    # 5. Use an if statement to check if the 'game_ready' variable is set to True
        
        # 6. Use background(color) to set the game's background
        # Do you see your color when you run the code?
        
        # 7. Use the draw_game_header() function to draw the game's header
        # Skip down and complete the draw_game_header() function
        
        # 8. Complete the instructions in draw_game_header() below FIRST!

        # 12. Use a for loop to go through each cell in the 'cells' list variable 
            
            # 13. Call each cell's draw() method
            # Do you see the grid of cells?

        
        # 14. Use the update_game_time() function to count the game seconds
        # when the game starts.
        # Does the game start counting up the seconds when the start button is pressed?

        
        # *** ENHANCEMENTS ***
        # * Changing the game background color?
        # * Can you figure out how to change the color of each cell?
        # * Adding difficulty modes that change the game's window size
        #   and number of mines.
        # * Changing the mine and flag images to something more fun!

#
# Draw top game header with # mines, start button, elapsed time
#            
def draw_game_header():
    pass
    # 9. Use the text("my text", x, y) function to draw the remaining number
    # of mines at the top of window
    #    - num_of_mines variable holds the total number of mines in the game
    #    - mines_flagged variable holds the number of mines that have been flagged
    #    - Use fill(color) to change the text color
    #    - Use textSize(int_size) to change the size of the text

    # 10. Use the text("my text", x, y) function to draw the game time
    #    - the 'game_time_sec' variable holds the number of seconds
    #      since the game started
    
    # 11. Call draw() from the start_button to draw the start button
    # Do you see the start button, mines left, and game timer?



# =================== DO NOT MODIFY THE CODE BELOW ======================

#
# Win or lose, reveal all cells
#
def game_end(state):
    global game_in_progress
    
    game_in_progress = False
    
    if state.lower() == "won":
        Cell.mine_img = Cell.won_img
        
    for c in cells:
        c.revealed = True
        
#
# Return the cell that the mouse is currently hovering over
#
def check_cell_pressed():
    cell = None
    
    for c in cells:
        if( c.x < mouseX and (c.x + cell_width) > mouseX and
            c.y < mouseY and (c.y + cell_width) > mouseY ):
            cell = c
            break
        
    return cell

#
# Setup cell size, images, and start button
#
def initialize_game_data():
    global rows, game_time_sec, start_button

    # Don't use height becuase it includes the game header
    rows = width / cell_width
    
    Cell.initialize_images()
    Cell.cell_width = cell_width
    game_time_sec = 0
    
    if start_button is None:
        start_button = Button("Start", (width / 2) - 50, 0, 100, cell_width)

#
# Setup cells, place mines, start game timer
#
def initialize_cells():
    global cells

    cells = list()
    for i in range(rows):
        for j in range(rows):
            cells.append( Cell(i, j, cell_color, header_height) )

#
# Randomize mines in cells, set number of surrounding mines
#
def initialize_mines():
    global mines_flagged, mines_placed, game_ready
    
    # Don't place any mines if more than the number of cells--invalid starting state
    if num_of_mines < (rows * rows):
        mines_flagged = 0
        mines_placed = 0
        
        while mines_placed != num_of_mines:
            rand_cell = cells[ int(random(0, (rows * rows))) ]
            
            if not rand_cell.mine:
                rand_cell.mine = True
                mines_placed += 1
                
        game_ready = True
    
    # Set number of mines around each cell, zero to eight
    for cell in cells:
        neighbors = get_neighbors(cell)
        mines = 0
        
        for neighbor in neighbors:
            if neighbor.mine:
                mines += 1
                
        cell.mines_around = mines
        
#
# Start game timer at the very end for best accuracy
#            
def start_game_timer():
    global now_ms
    now_ms = millis()

#
# Tracks game timer ~1 sec increments
#
def update_game_time():
    global game_time_sec, now_ms
    
    if game_in_progress:
        if millis() > now_ms + 1000:
            game_time_sec += 1
            now_ms = millis()
        
#
# Return list of all cells around specified cell
#
def get_neighbors(cell):
    neighbors = list()
    
    for c in cells:
        if( (c.i >= cell.i - 1) and (c.i <= cell.i + 1) and
            (c.j >= cell.j - 1) and (c.j <= cell.j + 1) ):
            neighbors.append(c)
            
    return neighbors

#
# Uncover cell (mine, number, or empty)
#
def reveal_cell(cell):
    cell.revealed = True
    
    # Hit mine, reveal all cells, game is over!
    if cell.mine:
        for c in cells:
            c.revealed = True        
        return

    # No mines around this cell, reveal all neighboring cells.
    # Do this until all neighboring cells with 0 surrounding mines are revealed
    if cell.mines_around == 0:
        neighbors = get_neighbors(cell)
        
        for c in neighbors:
            if not c.revealed:
                reveal_cell(c)

#
# Right mouse button: flag cell
# Left mouse button: reveal cell (mine, number, or empty)
#
def mousePressed():
    global game_in_progress, mines_flagged
    
    if start_button.mouse_is_over():
        game_in_progress = True
        initialize_game_data()
        initialize_cells()
        initialize_mines()
        start_game_timer()
        return
    elif not game_in_progress:
        # Don't allow clicking on the cells before pressing the start button
        return
    
    cell = check_cell_pressed()
    
    if cell is not None:
        if mouseButton == RIGHT:
            if not cell.revealed:
                cell.pinned = not cell.pinned
                if cell.pinned:
                    mines_flagged += 1
                else:
                    mines_flagged -= 1
            
        elif mouseButton == LEFT:
            # Don't reveal pinned/marked cells. User must unpin to reveal.
            if cell.pinned:
                return
            
            reveal_cell(cell)
            
            if cell.mine:
                game_end("Lost")
            else:
                # Check if player won the game,
                # i.e. there are no unrevealed empty cells
                
                cells_left = 0
                for c in cells:
                    if not c.mine and not c.revealed:
                        cells_left += 1
                        
                if cells_left == 0:
                    game_end("Won")
            
