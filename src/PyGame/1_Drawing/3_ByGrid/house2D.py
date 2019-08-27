# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "House")

# -*- acsection: main -*-
canvas.fill(pg.Color("lightblue")) # paint background

pg.draw.circle(canvas, pg.Color("orange"), (250, 180), 30)   # sun
pg.draw.rect(canvas, pg.Color("green"), (0, 200, 300, 100))  # grass
pg.draw.rect(canvas, pg.Color("brown"), (50, 150, 150, 100)) # house
pg.draw.polygon(canvas, pg.Color("red"), [(50, 150), (125, 100), (200, 150)]) # roof

# -*- acsection: after-main -*-
pygamebg.wait_loop()
