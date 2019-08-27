# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Tree")

# -*- acsection: main -*-
canvas.fill(pg.Color("white")) # paint background

# the colors we will use
GREEN = (0, 100, 36)
BROWN = (97, 26, 9)

# tree
pg.draw.rect(canvas, BROWN, (130, 250, 40, 50))
# treetop
pg.draw.polygon(canvas, GREEN, [(50, 250), (150, 150), (250, 250)])
pg.draw.polygon(canvas, GREEN, [(75, 200), (150, 100), (225, 200)])
pg.draw.polygon(canvas, GREEN, [(100, 150), (150, 50), (200, 150)])

# -*- acsection: after-main -*-
pygamebg.wait_loop()
