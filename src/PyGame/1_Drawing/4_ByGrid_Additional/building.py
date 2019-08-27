# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(400, 400, "Building")

# -*- acsection: main -*-
canvas.fill(pg.Color("lightgray")) # paint background

pg.draw.rect(canvas, pg.Color("darkgray"), (120, 50, 60, 140))   # building
pg.draw.rect(canvas, pg.Color("yellow"), (130, 60, 15, 15))      # left window, first row
pg.draw.rect(canvas, pg.Color("yellow"), (155, 60, 15, 15))      # right window, first row
pg.draw.rect(canvas, pg.Color("yellow"), (130, 80, 15, 15))      # left window, second row
pg.draw.rect(canvas, pg.Color("black"),  (155, 80, 15, 15))      # right window, second row
pg.draw.rect(canvas, pg.Color("black"),  (130, 100, 15, 15))     # left window, third row
pg.draw.rect(canvas, pg.Color("yellow"), (155, 100, 15, 15))     # right window, third row
pg.draw.rect(canvas, pg.Color("yellow"), (130, 120, 15, 15))     # left window, fourth row
pg.draw.rect(canvas, pg.Color("yellow"), (155, 120, 15, 15))     # right window, fourth row
pg.draw.rect(canvas, pg.Color("black"),  (130, 140, 15, 15))     # left window, fifth row
pg.draw.rect(canvas, pg.Color("black"),  (155, 140, 15, 15))     # right window, fifth row
pg.draw.rect(canvas, pg.Color("black"),  (140, 160, 20, 30))     # door

# -*- acsection: after-main -*-
pygamebg.wait_loop()
