# -*- acsection: general-init -*-
import pygame as pg, petljapg
canvas = petljapg.open_window(800, 600, "Apples")
# -*- acsection: main -*-

tree_image = pg.image.load("tree.png")  # image of a tree

canvas.fill(pg.Color("darkgreen"))
canvas.blit(tree_image, (0, 0))

# -*- acsection: after-main -*-
petljapg.wait_loop()
