# -*- acsection: general-init -*-
import pygame as pg, pygamebg
width, height = 300, 300
canvas = pygamebg.open_window(width, height, "Building - lights")

# -*- acsection: main -*-
canvas.fill(pg.Color("lightgray"))

pg.draw.rect(canvas, pg.Color("darkgray"), (120, 50, 60, 140))    # building

y = pg.Color('yellow')
b = pg.Color('black')
color = [y, y, y, b, b, y, y, y, b, b]
for i in range(5):
    pg.draw.rect(canvas, color[2*i],   (130, 60 + 20 * i, 15, 15)) # left window
    pg.draw.rect(canvas, color[2*i+1], (155, 60 + 20 * i, 15, 15)) # right window

pg.draw.rect(canvas, pg.Color("black"),  (140, 160, 20, 30))      # door

# -*- acsection: after-main -*-
pygamebg.wait_loop()
