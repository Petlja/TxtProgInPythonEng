# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Building")

# -*- acsection: main -*-
canvas.fill(pg.Color("lightgray"))

pg.draw.rect(canvas, pg.Color("darkgray"), (120, 50, 60, 140)) # buildnig

# windows
pg.draw.rect(canvas, pg.Color('yellow'), (130,  60, 15, 15))
pg.draw.rect(canvas, pg.Color('black'), (155,  60, 15, 15))
pg.draw.rect(canvas, pg.Color('black'), (130,  80, 15, 15))
pg.draw.rect(canvas, pg.Color('yellow'), (155,  80, 15, 15))
pg.draw.rect(canvas, pg.Color('yellow'), (130, 100, 15, 15))
pg.draw.rect(canvas, pg.Color('black'), (155, 100, 15, 15))
pg.draw.rect(canvas, pg.Color('black'), (130, 120, 15, 15))
pg.draw.rect(canvas, pg.Color('yellow'), (155, 120, 15, 15))
pg.draw.rect(canvas, pg.Color('yellow'), (130, 140, 15, 15))
pg.draw.rect(canvas, pg.Color('black'), (155, 140, 15, 15))

pg.draw.rect(canvas, pg.Color("black"),  (140, 160, 20, 30))   # door

# -*- acsection: after-main -*-
pygamebg.wait_loop()
