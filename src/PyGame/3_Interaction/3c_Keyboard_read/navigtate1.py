# -*- acsection: general-init -*-
import pygame as pg, pygamebg
width, height = 400, 400
canvas = pygamebg.open_window(width, height, "Navigate with the arrows")

x, y = width//2, height//2

def new_frame():
    global x, y

# -*- acsection: main -*-
    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT] and (x > 0):
        x -= 1
    if pressed[pg.K_RIGHT] and (x < width-1):
        x += 1
    if pressed[pg.K_UP] and (y > 0):
        y -= 1
    if pressed[pg.K_DOWN] and (y < height-1):
        y += 1
# -*- acsection: after-main -*-

    canvas.fill(pg.Color("black"))   # paint canvas to black
    pg.draw.circle(canvas, pg.Color('yellow'), (x, y), 20)
    
pygamebg.frame_loop(50, new_frame)
