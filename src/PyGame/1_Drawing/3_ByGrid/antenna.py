# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Antenna")

# -*- acsection: main -*-
canvas.fill(pg.Color("skyblue")) # paint background

pg.draw.line(canvas, pg.Color('black'), (150,  50), (150, 250), 4)
pg.draw.line(canvas, pg.Color('black'), (120,  75), (180,  75), 1)
pg.draw.line(canvas, pg.Color('black'), (110, 100), (190, 100), 1)
pg.draw.line(canvas, pg.Color('black'), (100, 125), (200, 125), 2)
pg.draw.line(canvas, pg.Color('black'), ( 90, 150), (210, 150), 2)
pg.draw.line(canvas, pg.Color('black'), ( 80, 175), (220, 175), 3)
pg.draw.line(canvas, pg.Color('black'), ( 70, 200), (230, 200), 3)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
