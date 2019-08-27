# -*- acsection: general-init -*-
import pygame as pg, pygamebg
width, height = 300, 300
canvas = pygamebg.open_window(width, height, "Bricks")

# -*- acsection: main -*-
canvas.fill(pg.Color("red"))
brick_width, brick_height = 80, 40
for y0 in range(0, height, 2 * brick_height):
    for x0 in range(0, width, brick_width):
        # draw the first brick
        pg.draw.rect(canvas, pg.Color("black"), (x0, y0, brick_width, brick_height), 1)
        
        # the second brick is in the following row, displaced by half its width
        x1, y1 = x0 - brick_width//2, y0 + brick_height 
        pg.draw.rect(canvas, pg.Color("black"), (x1, y1, brick_width, brick_height), 1)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
