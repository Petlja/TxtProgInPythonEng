# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(800, 600, "Apples")
# -*- acsection: main -*-

tree_image = pg.image.load("tree.png")  # image of a tree
apple_image = pg.image.load("apple_small.png")  # image of an apple
apple_positions = ((43,191), (61, 158), (124, 145), (134, 175), (160, 180))

canvas.fill(pg.Color("darkgreen"))
for tree_x, tree_y in ((0, 0), (200, 70), (120, 150), (240, 290), (550, 170), (400, 200)):
    canvas.blit(tree_image, (tree_x, tree_y))
    
for apple_x, apple_y in apple_positions:
    canvas.blit(apple_image, (apple_x, apple_y))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
