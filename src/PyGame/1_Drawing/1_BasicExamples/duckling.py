# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(400, 400, "Duckling")
# -*- acsection: main -*-

# paint background
canvas.fill(pg.Color("green"))

# draw head
pg.draw.ellipse(canvas, pg.Color("yellow"), (40, 50, 320, 300))
pg.draw.ellipse(canvas, pg.Color("black"), (40, 50, 320, 300), 1)
# draw eyes
pg.draw.ellipse(canvas, pg.Color("black"), (130, 130, 40, 40))
pg.draw.ellipse(canvas, pg.Color("black"), (280, 120, 40, 40))
# draw mouth (beak)
pg.draw.ellipse(canvas, pg.Color("red"), (200, 170, 120, 140))
pg.draw.ellipse(canvas, pg.Color("black"), (200, 170, 120, 140), 1)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
