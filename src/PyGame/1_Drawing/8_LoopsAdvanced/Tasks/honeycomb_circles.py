# -*- acsection: general-init -*-
import pygame as pg, pygamebg
width, height = 300, 300
canvas = pygamebg.open_window(width, height, "Honeycomb circles")
# -*- acsection: main -*-

canvas.fill((255,255,128))
for y0 in range(-17, height, 34):
    for x0 in range(-10, width, 60):
        pg.draw.circle(canvas, pg.Color("goldenrod"), (x0, y0), 16)
        pg.draw.circle(canvas, pg.Color("goldenrod"), (x0 + 30, y0 + 17), 16)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
