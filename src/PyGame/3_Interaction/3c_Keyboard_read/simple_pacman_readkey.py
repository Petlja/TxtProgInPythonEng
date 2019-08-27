import pygame as pg, pygamebg, random
num_rows, num_cols = 10, 10
a = 50 # square size
(width, height) = (a* num_cols, a * num_rows)
canvas = pygamebg.open_window(width, height, "Dot-eater")

(pacman_row, pacman_col) = (num_rows // 2, num_cols // 2)

def new_frame():
    global pacman_row, pacman_col

    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT] and (pacman_col > 0):           pacman_col -= 1
    if pressed[pg.K_RIGHT] and (pacman_col < num_cols-1): pacman_col += 1
    if pressed[pg.K_UP] and (pacman_row > 0):             pacman_row -= 1
    if pressed[pg.K_DOWN] and (pacman_row < num_rows-1):  pacman_row += 1

    # draw
    canvas.fill(pg.Color("black"))   # paint canvas 
    # white dots
    for x in range(a // 2, width, a):
        for y in range(a // 2, height, a):
            pg.draw.circle(canvas, pg.Color("white"), (x, y), 3)
   
    # draw pacman
    (x, y) = (pacman_col * a + a//2, pacman_row * a + a//2)
    pg.draw.circle(canvas, pg.Color('yellow'), (x, y), a // 3)
    
pygamebg.frame_loop(30, new_frame)
