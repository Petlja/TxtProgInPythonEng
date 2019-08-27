# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(800, 600, "Apples")
# -*- acsection: main -*-

tree_image = pg.image.load("tree.png")  # image of a tree
apple_image = pg.image.load("apple_small.png")  # image of an apple
apple_positions = ((43,191), (61, 158), (124, 145), (134, 175), (160, 180))

canvas.fill(pg.Color("darkgreen"))
canvas.blit(tree_image, (0, 0))
for x, y in apple_positions:
    canvas.blit(apple_image, (x, y))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
