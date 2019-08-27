# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Antenna")

# -*- acsection: main -*-
canvas.fill(pg.Color("skyblue")) # paint background

pg.draw.line(canvas, pg.Color('black'), (150,  50), (150, 250), 4)
for i in range(6):
    pg.draw.line(canvas, pg.Color('black'), (120 - 10 * i,  75 + 25 * i), (180 +  10 * i,  75 + 25 * i), 1 + i//2)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
