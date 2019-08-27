# -*- acsection: general-init -*-
import pygame as pg, petljapg
(width, height) = (500, 300)
canvas = petljapg.open_window(width, height, "Grid")

# -*- acsection: main -*-
canvas.fill(pg.Color("gray"))

for x in range(10, width, 20):
    pg.draw.line(canvas, pg.Color("black"), (x, 10), (x, height - 10), 1)

for y in range(10, height, 20):
    pg.draw.line(canvas, pg.Color("black"), (10, y), (width - 10, y), 1)

# -*- acsection: after-main -*-
petljapg.wait_loop()
