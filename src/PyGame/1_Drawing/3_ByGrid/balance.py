# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Balance")

# -*- acsection: main -*-
canvas.fill(pg.Color("green")) # paint background

pg.draw.line(canvas, pg.Color("brown"), (60, 100), (240,  100), 2)                              # beam
pg.draw.polygon(canvas, pg.Color("brown"), [(100, 120), (150, 100), (200, 120), (100, 120)])    # support
pg.draw.polygon(canvas, pg.Color("brown"), [( 30, 200), ( 60, 100), ( 90, 200), ( 30, 200)], 2) # left pan
pg.draw.polygon(canvas, pg.Color("brown"), [(210, 200), (240, 100), (270, 200), (210, 200)], 2) # right pan

# -*- acsection: after-main -*-
pygamebg.wait_loop()
