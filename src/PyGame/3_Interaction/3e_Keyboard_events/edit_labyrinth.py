import pygame as pg, pygamebg, random
a = 50 # square size
num_rows = 12
num_cols = 20
(width, height) = (num_cols * a, num_rows * a)
canvas = pygamebg.open_window(width, height, "Maze")

def new_frame():
    canvas.fill(pg.Color('white')) # paint background
    for row in range(num_rows):
        for col in range(num_cols):
            if board[row][col] == 1: # wall
                pg.draw.rect(canvas, pg.Color('black'), (col * a, row * a, a, a))

    # frame
    pg.draw.rect(canvas, pg.Color('red'), (frame_col * a, frame_row * a, a, a), 3)
    
def handle_event(event):
    global board, frame_row, frame_col
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
            board[frame_row][frame_col] = 1 - board[frame_row][frame_col]

board = []
for j in range(num_rows):
    board.append([])
    for i in range(num_cols):
        board[-1].append(random.randint(0, 1))
        
(frame_row, frame_col) = (0, 0)
pygamebg.frame_loop(10, new_frame, handle_event)
