# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (200, 200)
canvas = pygamebg.open_window(width, height, "Three circles")
# -*- acsection: main -*-

canvas.fill(pg.Color("white")) # paint background
(cx, cy) = (width // 2, height // 2) # the center of the circles is in the middle of the window
pg.draw.circle(canvas, pg.Color("red"), (cx, cy), 100)   # red circle
pg.draw.circle(canvas, pg.Color("blue"), (cx, cy), 75)   # blue circle
pg.draw.circle(canvas, pg.Color("green"), (cx, cy), 50)  # green circle

# -*- acsection: after-main -*-
pygamebg.wait_loop()
