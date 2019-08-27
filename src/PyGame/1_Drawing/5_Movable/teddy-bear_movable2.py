# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (500, 300)
canvas = pygamebg.open_window(width, height, "Teddy-bear")
# -*- acsection: main -*-

canvas.fill(pg.Color("white")) # paint background
YELLOW = pg.Color("yellow")
BLACK  = pg.Color("black")

def draw_teddy(cx, cy):
    teddy = (
        #color, (  x,   y),  r
        (YELLOW, (-60, -60),  45), # left ear
        (YELLOW, ( 60, -60),  45), # right ear
        (YELLOW, (  0,   0), 100), # head
        (YELLOW, (  0,  50),  50), # snout
        (BLACK, (-50, -30),  15), # left eye
        (BLACK, ( 50, -30),  15), # right eye
        (BLACK, (  0,  20),  15), # snout top
    )
    for color, (dx, dy), radius in teddy:
        centar = (cx + dx, cy + dy)
        pg.draw.circle(canvas, color, centar, radius)
        pg.draw.circle(canvas, BLACK, centar, radius, 1)

draw_teddy(width // 2, height // 2)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
