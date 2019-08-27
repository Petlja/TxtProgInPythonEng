# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "House")

# -*- acsection: main -*-
canvas.fill(pg.Color("darkgreen")) # paint background

pg.draw.polygon(canvas, pg.Color("red"), [(50, 150), (120, 100), (190, 150)]) # roof
pg.draw.rect(canvas, pg.Color("khaki"), ( 50, 150, 140, 100))  # walls
pg.draw.rect(canvas, pg.Color("brown"), ( 60, 170,  30,  30))  # left window
pg.draw.rect(canvas, pg.Color("brown"), (150, 170,  30,  30))  # right window
pg.draw.rect(canvas, pg.Color("brown"), (100, 180,  40,  70))  # door

# -*- acsection: after-main -*-
pygamebg.wait_loop()
