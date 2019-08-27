# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Teddy-bear")
# -*- acsection: main -*-

canvas.fill(pg.Color("white")) # paint background
YELLOW = pg.Color("yellow")
BLACK = pg.Color("black")

def draw_teddy(cx, cy, a):
    teddy = (
        #color, (  x,   y),  r
        (YELLOW, (-12, -12),  9), # left ear
        (YELLOW, ( 12, -12),  9), # right ear
        (YELLOW, (  0,   0), 20), # head
        (YELLOW, (  0,  10), 10), # snout
        (BLACK,  (-10,  -6),  3), # left eye
        (BLACK,  ( 10,  -6),  3), # right eye
        (BLACK,  (  0,   4),  3), # snout top
    )
    for color, (dx, dy), radius in teddy:
        center = (cx + dx*a, cy + dy*a)
        pg.draw.circle(canvas,  color, center, a*radius)
        pg.draw.circle(canvas, BLACK, center, a*radius, 1)

draw_teddy(85, 100, 4)
draw_teddy(235, 100, 3)
draw_teddy(50, 250, 2)
draw_teddy(150, 250, 2)
draw_teddy(250, 250, 2)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
