# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Trees")

# -*- acsection: main -*-
canvas.fill(pg.Color("green")) # paint background

for i in range(3):
    pg.draw.rect(canvas, pg.Color("brown"), (100*i + 40, 180, 20, 100))        # tree
    pg.draw.ellipse(canvas, pg.Color("darkgreen"), (100*i + 10, 50, 80, 150))  # treetop

# -*- acsection: after-main -*-
pygamebg.wait_loop()
