# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Emoticon")

# -*- acsection: main -*-
canvas.fill(pg.Color("white")) # paint background

pg.draw.circle(canvas, pg.Color("yellow"), (150, 150), 100) # head
pg.draw.ellipse(canvas, pg.Color("black"), (100, 90, 30, 60)) # left eye
pg.draw.ellipse(canvas, pg.Color("black"), (170, 90, 30, 60)) # right eye
pg.draw.ellipse(canvas, pg.Color("white"), (100, 190, 100, 20)) # the inside of the mouth
pg.draw.ellipse(canvas, pg.Color("black"), (100, 190, 100, 20), 2) # the edge of the mouth

# -*- acsection: after-main -*-
pygamebg.wait_loop()
