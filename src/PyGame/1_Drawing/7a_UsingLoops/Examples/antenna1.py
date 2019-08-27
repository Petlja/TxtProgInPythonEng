# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Antenna")

# -*- acsection: main -*-
canvas.fill(pg.Color("skyblue")) # paint background

pg.draw.line(canvas, pg.Color('black'), (150,  50), (150, 250), 4)
x1, x2, y, thickness = 120, 180, 75, 1.0
for i in range(6):
    pg.draw.line(canvas, pg.Color('black'), (x1, y), (x2, y), int(thickness))
    x1 -= 10
    x2 += 10
    y += 25
    thickness += 0.5

# -*- acsection: after-main -*-
pygamebg.wait_loop()
