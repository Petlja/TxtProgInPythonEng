# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (300, 300)
canvas = pygamebg.open_window(width, height, "Bricks")

# -*- acsection: main -*-
canvas.fill(pg.Color("red"))
brick_width, brick_height = 80, 40
x_start = 0 # x coordinates of the first brick in the first row
for y0 in range(0, height, brick_height):
    for x0 in range(x_start, width, brick_width):
        pg.draw.rect(canvas, pg.Color("black"), (x0, y0, brick_width, brick_height), 1)
        
    # preparing to draw the next row of bricks
    if x_start == 0: # x_start is the opposite of the previous one
        x_start = -brick_width//2
    else:
        x_start = 0

# -*- acsection: after-main -*-
pygamebg.wait_loop()
