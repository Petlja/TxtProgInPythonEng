# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (300, 300)
canvas = pygamebg.open_window(width, height, "Circles")
# -*- acsection: main -*-

canvas.fill(pg.Color("white")) # paint background

# the center of the circle is in the center of the window
center = (width // 2, height // 2)

# drawing circles
# the radius changes from 25 to 150, with step 25
pg.draw.circle(canvas, pg.Color("red"), center,  25, 2)
pg.draw.circle(canvas, pg.Color("red"), center,  50, 2)
pg.draw.circle(canvas, pg.Color("red"), center,  75, 2)
pg.draw.circle(canvas, pg.Color("red"), center, 100, 2)
pg.draw.circle(canvas, pg.Color("red"), center, 125, 2)
pg.draw.circle(canvas, pg.Color("red"), center, 150, 2)
# -*- acsection: after-main -*-
pygamebg.wait_loop()
