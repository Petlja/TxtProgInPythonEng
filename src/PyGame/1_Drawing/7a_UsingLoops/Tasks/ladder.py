# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (300, 300)
canvas = pygamebg.open_window(width, height, "Ladder")

# -*- acsection: main -*-
canvas.fill(pg.Color("green")) # paint background

pg.draw.line(canvas, pg.Color("brown"), (100, 10), (100, height - 10), 10)    # left side
pg.draw.line(canvas, pg.Color("brown"), (200, 10), (200, height - 10), 10)    # right side

for i in range(1, 6):
    pg.draw.line(canvas, pg.Color("brown"), (100, i * 50), (200, i * 50), 10) # step

# -*- acsection: after-main -*-
pygamebg.wait_loop()
