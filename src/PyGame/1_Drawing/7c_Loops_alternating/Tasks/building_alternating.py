# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Building")

# -*- acsection: main -*-
canvas.fill(pg.Color("lightgray"))

pg.draw.rect(canvas, pg.Color("darkgray"), (120, 50, 60, 140)) # building

for y in range(5):     # floor
    for x in range(2): # side (0 - left, 1 - right)
        if (x+y) % 2 == 0:
            color = pg.Color("yellow")
        else:
            color = pg.Color("black")
        square = (130 + 25 * x, 60 + 20 * y, 15, 15)
        pg.draw.rect(canvas, color, square)                    # window

pg.draw.rect(canvas, pg.Color("black"),  (140, 160, 20, 30))   # door

# -*- acsection: after-main -*-
pygamebg.wait_loop()
