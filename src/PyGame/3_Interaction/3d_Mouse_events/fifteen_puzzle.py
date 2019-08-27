import pygame as pg, pygamebg, random
(width, height) = (400, 400)
canvas = pygamebg.open_window(width, height, "15 puzzle")

# move hole to (row, col) if possible
def move_hole(row, col):
    global hole_row, hole_col, puzzle     # global variables that wil be modified
    if 0 <= row and row < BOARD_SIZE and \
       0 <= col and col < BOARD_SIZE:    # square has to be inside board
        (d_row, d_col) = (abs(row - hole_row), abs(col - hole_col)) 
        # square must be adjacent to the hole
        if (d_row == 1 and d_col == 0) or (d_row == 0 and d_col == 1):
            (puzzle[hole_row][hole_col], puzzle[row][col]) = \
            (puzzle[row][col], puzzle[hole_row][hole_col])      # exchange numbers on hole and on square
            (hole_row, hole_col) = (row, col)                   # move hole
            return True                                         # we successfully moved the hole
    return False                                                # we were unable to move the hole

# randomly mix the puzzle
def mix_the_puzzle():
    global hole_row, hole_col, puzzle                            # global variables that will be modified
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]              # displacements for the four possible directions
    max_num_moves = 100                                          # mix by moving the hole 100 times
    num_moves = 0                                                # the number of moves made
    while num_moves < max_num_moves:                             # while the number of moves made is less than the maximum
        (d_row, d_col) = directions[random.randint(0, 3)]        # randomly choose the direction in which the hole moves
        (row, col) = (hole_row + d_row, hole_col + d_col)        # we determine the new possible hole position
        if move_hole(row, col):                                  # try moving hole to a new square
            num_moves += 1                                       # if succeed, increase the number of moves

# check if puzzle is solved
def puzzle_solved():
    # check if there is a square with the wrong number
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if puzzle[row][col] != row*BOARD_SIZE+col+1:
                return False  # number at square[row][col] is wrong
    return True  # we didn't find a wrong number

BOARD_SIZE = 4                        # puzzle is 4x4 squares
COL_WIDTH = width // BOARD_SIZE  # column width in pixels
ROW_HEIGHT = height // BOARD_SIZE   # row height in pixels

# we initially fill the puzzle with numbers 1 through n * n
puzzle = [[BOARD_SIZE*row + col + 1 for col in range(BOARD_SIZE)] for row in range(BOARD_SIZE)] 
(hole_row, hole_col) = (BOARD_SIZE-1, BOARD_SIZE-1)        # the blank field is in the lower right corner
mix_the_puzzle()                                           # mix the puzzle before the game starts


def display_puzzle():
    canvas.fill(pg.Color("white"))        # paint background
    font = pg.font.SysFont("Arial", 40)   # font for displaying numbers
    # go through all the squares
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            rect = (col*COL_WIDTH, row*ROW_HEIGHT, COL_WIDTH, ROW_HEIGHT)  # rectange around current square
            if row == hole_row and col == hole_col:                        # current square is the hole
                pg.draw.rect(canvas, pg.Color("black"), rect)              # draw hole as a filled black square
            else:
                pg.draw.rect(canvas, pg.Color("black"), rect, 1)           # draw square border
                (xc, yc) = (col*COL_WIDTH + COL_WIDTH/2, row*ROW_HEIGHT + ROW_HEIGHT/2) # square centar
                text = font.render(str(puzzle[row][col]), True, pg.Color("black"))      # display centered text
                (text_width, text_height) = (text.get_width(), text.get_height())
                canvas.blit(text, (xc - text_width/2, yc - text_height/2))

def congratulate():
    canvas.fill(pg.Color("white"))             # paint window
    font = pg.font.SysFont("Arial", 60)        # font for displaying text
    message = "Well done!"                     # message to be displayed
    text_image = font.render(message, True, pg.Color("black"))  
    (text_width, text_height) = (text_image.get_width(), text_image.get_height()) # determine text size
    (x, y) = ((width - text_width) / 2, (height - text_height) / 2)    # we set position so that text is centered
    canvas.blit(text_image, (x, y))                                    # display text image at approptiate position

def new_frame():
    if not puzzle_solved(): # puzzle not solved yet, displayi it
        display_puzzle()
    else:  # puzzle is solved, congratulating
        congratulate()
                
def handle_event(event):
    global row, col, puzzle
    if puzzle_solved():  # if puzzle is solved, don't handle events
        return
    if event.type == pg.MOUSEBUTTONDOWN:  # mouse click
        (x, y) = event.pos                # the coordinates that were clicked
        row = y // ROW_HEIGHT             # row that were clicked
        col = x // COL_WIDTH              # column that were clicked
        move_hole(row, col)
                
pygamebg.frame_loop(15, new_frame, handle_event)
