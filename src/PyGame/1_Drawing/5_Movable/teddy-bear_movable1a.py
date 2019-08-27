# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (500, 300)
canvas = pygamebg.open_window(width, height, "Teddy-bear")
# -*- acsection: main -*-

canvas.fill(pg.Color("white")) # paint background

def framed_circle(canvas, color, center, radius):
    pg.draw.circle(canvas, color, center, radius)
    pg.draw.circle(canvas, pg.Color("black"), center, radius, 1)

def draw_teddy(cx, cy):
    framed_circle(canvas, pg.Color("yellow"), (cx - 60,  cy - 70),  45) # left ear
    framed_circle(canvas, pg.Color("yellow"), (cx + 60,  cy - 70),  45) # right ear
    framed_circle(canvas, pg.Color("yellow"), (cx,       cy),      100) # head
    framed_circle(canvas, pg.Color("yellow"), (cx,       cy + 50),  50) # snout
    framed_circle(canvas, pg.Color("black"),  (cx - 50,  cy - 30),  15) # left eye
    framed_circle(canvas, pg.Color("black"),  (cx + 50,  cy - 30),  15) # right eye
    framed_circle(canvas, pg.Color("black"),  (cx,       cy + 20),  15) # snout top

draw_teddy(width // 2, height // 2)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
