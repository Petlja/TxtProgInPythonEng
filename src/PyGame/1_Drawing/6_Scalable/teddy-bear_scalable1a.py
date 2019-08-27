# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (300, 300)
canvas = pygamebg.open_window(width, height, "Teddy-bear")
# -*- acsection: main -*-

canvas.fill(pg.Color("white")) # paint background

def framed_circle(canvas, color, center, radius):
    pg.draw.circle(canvas, color, center, radius)
    pg.draw.circle(canvas, pg.Color("black"), center, radius, 1)

def draw_teddy(cx, cy, a):
    framed_circle(canvas, pg.Color("yellow"), (cx - 12*a,  cy - 14*a),  9*a) # left ear
    framed_circle(canvas, pg.Color("yellow"), (cx + 12*a,  cy - 14*a),  9*a) # right ear
    framed_circle(canvas, pg.Color("yellow"), (cx,         cy),        20*a) # head
    framed_circle(canvas, pg.Color("yellow"), (cx,         cy + 10*a), 10*a) # snout
    framed_circle(canvas, pg.Color("black"),  (cx - 10*a,  cy - 6*a),   3*a) # left eye
    framed_circle(canvas, pg.Color("black"),  (cx + 10*a,  cy - 6*a),   3*a) # right eye
    framed_circle(canvas, pg.Color("black"),  (cx,         cy + 4*a),   3*a) # snout top

draw_teddy(width // 2, height // 2, 6)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
