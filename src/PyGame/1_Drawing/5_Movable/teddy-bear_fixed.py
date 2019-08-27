# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(500, 300, "Teddy-bear")
# -*- acsection: main -*-

canvas.fill(pg.Color("white")) # paint background

def framed_circle(canvas, color, center, radius):
    pg.draw.circle(canvas, color, center, radius)
    pg.draw.circle(canvas, pg.Color("black"), center, radius, 1)
   
framed_circle(canvas, pg.Color("yellow"), (190,  80),  45) # left ear
framed_circle(canvas, pg.Color("yellow"), (310,  80),  45) # right ear
framed_circle(canvas, pg.Color("yellow"), (250, 150), 100) # head
framed_circle(canvas, pg.Color("yellow"), (250, 200),  50) # snout
framed_circle(canvas, pg.Color("black"),  (200, 120),  15) # left eye
framed_circle(canvas, pg.Color("black"),  (300, 120),  15) # right eye
framed_circle(canvas, pg.Color("black"),  (250, 170),  15) # snout top

# -*- acsection: after-main -*-
pygamebg.wait_loop()
