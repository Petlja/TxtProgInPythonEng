import pygame as pg, pygamebg, random
num_rows, num_cols = 10, 10
a = 50 # squaer size
(width, height) = (a* num_cols, a * num_rows)
canvas = pygamebg.open_window(width, height, "Dot-eater")

there_is_a_dot = []
for _ in range(num_rows):
    there_is_a_dot.append([True] * num_cols)

(pacman_row, pacman_col) = (num_rows // 2, num_cols // 2)

def draw():
    canvas.fill(pg.Color("gray"))   # paint canvas
    
    # draw dots
    for row in range(num_rows):
        for col in range(num_cols):
            if there_is_a_dot[row][col]:
                (x, y) = (col * a + a//2, row * a + a//2)
                pg.draw.circle(canvas, pg.Color('white'), (x, y), 5)
                
    # draw pacman
    (x, y) = (pacman_col * a + a//2, pacman_row * a + a//2)
    pg.draw.circle(canvas, pg.Color('yellow'), (x, y), a // 3)

def new_frame():
    global pacman_row, pacman_col
    
    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT] and (pacman_col > 0): 
        pacman_col -= 1
    if pressed[pg.K_RIGHT] and (pacman_col < num_cols-1):
        pacman_col += 1
    if pressed[pg.K_UP] and (pacman_row > 0):
        pacman_row -= 1
    if pressed[pg.K_DOWN] and (pacman_row < num_rows-1):
        pacman_row += 1

    there_is_a_dot[pacman_row][pacman_col] = False # dot eaten
    
    draw()   
    
pygamebg.frame_loop(15, new_frame)
