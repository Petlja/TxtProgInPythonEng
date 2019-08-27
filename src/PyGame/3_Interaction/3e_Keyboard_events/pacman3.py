import pygame as pg, pygamebg, random
board = [
    '.........',
    '...XXX...',
    '..XXXXX..',
    '.........',
    '.........'
]
num_rows = len(board)
num_cols = len(board[0])
a = 50 # square size
(width, height) = (a* num_cols, a * num_rows)
canvas = pygamebg.open_window(width, height, "Dot-eater")

(pacman_row, pacman_col) = (num_rows // 2, num_cols // 2)
(d_row, d_col) = (0, 0)

def new_frame():
    global pacman_row, pacman_col
    new_row = pacman_row + d_row
    new_col = pacman_col + d_col
    if (new_col >= 0 and new_col < num_cols
        and new_row >= 0 and new_row < num_rows
        and board[new_row][new_col] == '.'):
        pacman_col = new_col
        pacman_row = new_row

    canvas.fill(pg.Color("black"))   # paint canvas

    # board
    for row in range(num_rows):
        for col in range(num_cols):
            x, y = a * col, a * row
            if board[row][col] == 'X':
                pg.draw.rect(canvas, pg.Color("blue"), (x, y, a, a), 3)
            else:
                pg.draw.circle(canvas, pg.Color("white"), (x+a//2, y+a//2), 3)
   
    # draw pacman
    (x, y) = (pacman_col * a + a//2, pacman_row * a + a//2)
    pg.draw.circle(canvas, pg.Color('yellow'), (x, y), a // 3)
    
def handle_event(event):
    global pacman_row, pacman_col, d_row, d_col
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            d_row, d_col = 0, -1
        elif event.key == pg.K_RIGHT:
            d_row, d_col = 0, 1
        elif event.key == pg.K_UP:
            d_row, d_col = -1, 0
        elif event.key == pg.K_DOWN:
            d_row, d_col = 1, 0
        # else:
            # d_row, d_col = 0, 0

pygamebg.frame_loop(10, new_frame, handle_event)
