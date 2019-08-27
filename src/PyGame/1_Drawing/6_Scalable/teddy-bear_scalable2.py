# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (300, 300)
canvas = pygamebg.open_window(width, height, "Teddy-bear")
# -*- acsection: main -*-

canvas.fill(pg.Color("white")) # paint background
YELLOW = pg.Color("yellow")
BLACK = pg.Color("black")

def draw_teddy(cx, cy, a):
    teddy = (
        #boja, (  x,   y),  r
        (YELLOW, (-12, -12),  9), # left ear
        (YELLOW, ( 12, -12),  9), # right ear
        (YELLOW, (  0,   0), 20), # head
        (YELLOW, (  0,  10), 10), # snout
        (BLACK, (-10,  -6),  3), # left eye
        (BLACK, ( 10,  -6),  3), # right eye
        (BLACK, (  0,   4),  3), # snout top
    )
    for color, (dx, dy), radius in teddy:
        center = (cx + dx*a, cy + dy*a)
        pg.draw.circle(canvas, color, center, a*radius)
        pg.draw.circle(canvas, BLACK, center, a*radius, 1)

draw_teddy(width // 2, height // 2, 6)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
