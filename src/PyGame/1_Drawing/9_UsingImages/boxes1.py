# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(800, 600, "Boxes 1")
# -*- acsection: main -*-

box_image = pg.image.load("box.png")  # image of a box

canvas.fill(pg.Color("lightgray"))

for i in range(4):
    canvas.blit(box_image, (60+120*i, 400))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
