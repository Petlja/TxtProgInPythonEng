# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(800, 600, "Boxes 3")
# -*- acsection: main -*-

box_image = pg.image.load("box.png")  # image of a box

canvas.fill(pg.Color("lightgray"))

for ix in range(4):
    for iy in range(ix+1):
        canvas.blit(box_image, (60+120*ix, 400-95*iy))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
