# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(800, 600, "Apples")
# -*- acsection: main -*-

tree_image = pg.image.load("tree.png")  # image of a tree

canvas.fill(pg.Color("darkgreen"))
for tree_x, tree_y in ((200, 70), (120, 150), (240, 290), (550, 170), (400, 200)):
    canvas.blit(tree_image, (tree_x, tree_y))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
