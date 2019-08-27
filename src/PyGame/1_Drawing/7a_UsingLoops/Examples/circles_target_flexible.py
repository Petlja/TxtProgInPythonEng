# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (300, 300)
canvas = pygamebg.open_window(width, height, "Circles")
# -*- acsection: main -*-

canvas.fill(pg.Color("white")) # paint background

# the center of the circle is in the center of the window
center = (width // 2, height // 2)
num_circles = 6
r_step = width / (2*num_circles)

for i in range(1, num_circles + 1):
    pg.draw.circle(canvas, pg.Color("red"), center, round(i * r_step), 2)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
