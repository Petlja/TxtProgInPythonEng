# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(20, 40, "ladder")

# -*- acsection: main -*-
canvas.fill(pg.Color("white")) # paint background

pg.draw.line(canvas, pg.Color("black"), ( 5, 3), ( 5, 36), 1)  # left side
pg.draw.line(canvas, pg.Color("black"), (14, 3), (14, 36), 1)  # right side

pg.draw.line(canvas, pg.Color("black"), (5,  9), (14,  9), 1) # step
pg.draw.line(canvas, pg.Color("black"), (5, 16), (14, 16), 1) # step
pg.draw.line(canvas, pg.Color("black"), (5, 23), (14, 23), 1) # step
pg.draw.line(canvas, pg.Color("black"), (5, 30), (14, 30), 1) # step

# -*- acsection: after-main -*-
pygamebg.wait_loop()
