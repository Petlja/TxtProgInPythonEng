# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Trees")

# -*- acsection: main -*-
canvas.fill(pg.Color("green")) # paint background

pg.draw.rect(canvas, pg.Color("brown"), (40, 180, 20, 100))        # first tree
pg.draw.ellipse(canvas, pg.Color("darkgreen"), (10, 50, 80, 150))  # first treetop
pg.draw.rect(canvas, pg.Color("brown"), (140, 180, 20, 100))       # second tree
pg.draw.ellipse(canvas, pg.Color("darkgreen"), (110, 50, 80, 150)) # second treetop
pg.draw.rect(canvas, pg.Color("brown"), (240, 180, 20, 100))       # third tree
pg.draw.ellipse(canvas, pg.Color("darkgreen"), (210, 50, 80, 150)) # third treetop

# -*- acsection: after-main -*-
pygamebg.wait_loop()
