import pygame as pg, pygamebg, random
a = 50 # square size
num_rows = 12
num_cols = 20
(width, height) = (num_cols * a, num_rows * a)
canvas = pygamebg.open_window(width, height, "Maze")

def draw():
    # draw empty board
    canvas.fill(pg.Color('white'))
    for row in range(num_rows):
        for col in range(num_cols):
            if board[row][col] == -1: # wall
                pg.draw.rect(canvas, pg.Color('black'), (col * a, row * a, a, a))
            elif board[row][col] == 1: # current path
                pg.draw.circle(canvas, pg.Color('gray'), (col * a + a//2, row * a + a//2), 10)
            elif board[row][col] == 2: # were there and came back
                pg.draw.circle(canvas, pg.Color('black'), (col * a + a//2, row * a + a//2), 10)
    
    if not searching:
        pg.draw.rect(canvas, pg.Color('red'), (frame_col * a, frame_row * a, a, a), 3)
    

def new_frame():
    if searching and not paused:
        next(positions, 0)
    draw()
        
def handle_event(event):
    global paused, found, searching, positions, board, frame_row, frame_col
    if event.type == pg.KEYDOWN: # keystroke on the keyboard
        if event.key == pg.K_LEFT:
            if frame_col > 0:
                frame_col -= 1
        elif event.key == pg.K_RIGHT:
            if frame_col < num_cols-1:
                frame_col += 1
        elif event.key == pg.K_UP:
            if frame_row > 0:
                frame_row -= 1
        elif event.key == pg.K_DOWN:
            if frame_row < num_rows-1:
                frame_row += 1
        elif event.key == pg.K_SPACE:
            if (board[frame_row][frame_col] == 0) :
                board[frame_row][frame_col] = -1
            else: 
                board[frame_row][frame_col] = 0

        if chr(event.key) == 's': # (re)start
            for row in range(num_rows):
                for col in range(num_cols):
                    if board[row][col] > 0:
                        board[row][col] = 0
            searching = True
            found = False
            positions = seek(start[0], start[1]) # generator
        if chr(event.key) == 'p': # paused
            if searching:
                paused = not paused

def seek(x, y):
    global found
    if found: return
    if (x < 0 or y < 0 or x >= num_cols or y >= num_rows): return
    if (board[y][x] != 0): return

    board[y][x] = 1
    yield
    if (x, y) == target:
        found = True
        return

    yield from seek(x + 1, y)
    yield from seek(x - 1, y)
    yield from seek(x, y + 1)
    yield from seek(x, y - 1)

    if not found:
        board[y][x] = 2
        yield

FPS = 5
paused = False
start, target = (0,0), (num_cols-1, num_rows-1)
board = [[random.randint(-1, 0) for i in range(num_cols)]  for j in range(num_rows)]
(frame_row, frame_col) = (0, 0)
searching = False
found = False

pygamebg.frame_loop(FPS, new_frame, handle_event)
