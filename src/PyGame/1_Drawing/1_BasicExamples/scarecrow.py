# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 500, "Scarecrow")
# -*- acsection: main -*-

canvas.fill(pg.Color("white")) # paint background

pg.draw.circle(canvas, pg.Color("black"), (150, 70), 50, 6)        # head
pg.draw.line(canvas, pg.Color("black"), (150, 120), (150, 300), 6) # body
pg.draw.line(canvas, pg.Color("black"), (80, 170), (220, 170), 6)  # hands
pg.draw.line(canvas, pg.Color("black"), (150, 300), (90, 480), 6)  # left leg
pg.draw.line(canvas, pg.Color("black"), (150, 300), (210, 480), 6) # right leg

# -*- acsection: after-main -*-
pygamebg.wait_loop()
